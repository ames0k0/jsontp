import pytest

from jsontp import JsonTreeParser
from jsontp.config import Tree


def test_simple_data():
    data = {"a": 1, "b": 2}

    with pytest.raises(StopIteration):
        assert next(
            JsonTreeParser(data=data).tree_by_key_or_view(
                data=data,
                key="c",
            )
        )


def test_nested_simple_data():
    data = {"a": 1, "b": 2, "d": {"c": 3}}

    assert next(
        JsonTreeParser(data=data).tree_by_key_or_view(
            data=data,
            key="c",
        )
    ) == JsonTreeParser.join_tree(
        tree=JsonTreeParser.join_tree(
            tree=Tree.ROOT,
            key="d",
        ),
        key="c",
    )


def test_simple_data_with_list():
    data = {"a": 1, "b": 2, "d": [{"c": 3}]}

    assert next(
        JsonTreeParser(data=data).tree_by_key_or_view(
            data=data,
            key="c",
        )
    ) == JsonTreeParser.join_tree(
        tree=JsonTreeParser.join_tree(
            tree=Tree.ROOT,
            key="d",
        ),
        key="c",
        list_index=0,
    )


def test_simple_data_with_none():
    data = {"a": 1, "b": None, None: 4, "d": [{"c": 3}]}

    assert next(
        JsonTreeParser(data=data).tree_by_key_or_view(
            data=data,
            key="c",
        )
    ) == JsonTreeParser.join_tree(
        tree=JsonTreeParser.join_tree(
            tree=Tree.ROOT,
            key="d",
        ),
        key="c",
        list_index=0,
    )


def test_simple_data_for_noreturn():
    data = {"a": 1, "b": None, None: 4, "d": [{"c": 3}]}

    assert (
        next(
            JsonTreeParser(data=data).tree_by_key_or_view(
                data=data,
                key="c",
                result_to="print",
            )
        )
        is None
    )


def test_simple_data_value_with_list_index():
    data = {"a": 1, "b": 2, "d": [{"c": 3}]}

    # 'root -> d -> [0] -> c'
    tree = JsonTreeParser.join_tree(
        tree=JsonTreeParser.join_tree(
            tree=Tree.ROOT,
            key="d",
        ),
        key="c",
        list_index=0,
    )

    assert JsonTreeParser(data=data).data_by_tree(tree=tree) == 3
