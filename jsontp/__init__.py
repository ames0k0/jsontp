import typing
import json

from . import config


class JsonTreeParser:
    def __init__(self, data: json.loads):
        self.data = data

    @staticmethod
    def join_tree(
        *,
        tree: str,
        key: str | None,
        list_index: typing.Optional[int] = None,
    ) -> str:
        keys = [tree]

        if list_index is not None:
            keys.append(
                config.Tree.LIST_INDEX_WRAPPER.format(index=list_index),
            )

        keys.append(str(key))

        return config.Tree.DELIMITER.join(keys)

    def process_result(
        self,
        *,
        result: str,
        result_to: str,
        result_value: str,
    ) -> typing.Union[typing.Optional[str], typing.NoReturn]:
        if config.Tree.SEARCH_FILTER_KEY and (
            config.Tree.SEARCH_FILTER_KEY not in result
        ):
            return None

        if config.Tree.SEARCH_FILTER_VALUE:
            if not isinstance(result_value, (int, str)):
                return None
            if str(result_value) != config.Tree.SEARCH_FILTER_VALUE:
                return None

        if config.Tree.SEARCH_LIMIT > 0:
            config.Tree.SEARCH_LIMIT -= 1

        if config.Tree.SEARCH_LIMIT == 0:
            exit()

        if result_to == config.Key.SHOW:
            print(result)

        if result_to == config.Key.SAVE:
            return result

    def tree_by_key_or_view(
        self,
        *,
        data: typing.Optional[dict] = None,
        key: str = "",
        view: bool = False,
        gen_tree: str = config.Tree.ROOT,
        list_index: typing.Optional[int] = None,
        result_to: str = config.Key.SAVE,
    ) -> typing.Generator[str, None, None]:
        """Yields str: ex. A -> B -> C -> *key"""
        if data is None:
            data = self.data

        if isinstance(data, list):
            if config.Tree.SEARCH_ITEMS_LIMIT > 0:
                data = data[: config.Tree.SEARCH_ITEMS_LIMIT]
            for idx, item in enumerate(data):
                yield from self.tree_by_key_or_view(
                    data=item,
                    key=key,
                    view=view,
                    gen_tree=gen_tree,
                    list_index=idx,
                    result_to=result_to,
                )

        if isinstance(data, dict):
            for data_key, data_value in data.items():
                tree = self.join_tree(
                    tree=gen_tree,
                    key=data_key,
                    list_index=list_index,
                )

                if (data_key == key) or view:
                    yield self.process_result(
                        result=tree,
                        result_to=result_to,
                        result_value=data_value,
                    )
                    if not view:
                        continue

                if not view:
                    if data_key is None:
                        continue
                    elif data_value is None:
                        continue

                yield from self.tree_by_key_or_view(
                    data=data_value,
                    key=key,
                    view=view,
                    gen_tree=tree,
                    result_to=result_to,
                )

    def data_by_tree(
        self,
        *,
        tree: str,
    ) -> typing.Dict[typing.Any, typing.Any]:
        if config.Tree.ROOT:
            tree = tree.replace(
                self.join_tree(tree=config.Tree.ROOT, key=""),
                "",
                1,
            )

        tree_keys = tree.split(config.Tree.DELIMITER)
        inner_data = self.data

        for key in tree_keys:
            if key.startswith(config.Tree.LIST_INDEX_WRAPPER[0]):
                inner_data = inner_data[int(key[1:-1])]
            else:
                inner_data = inner_data[key]

        return inner_data
