#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from typing import Optional
from pprint import pprint

from . import config
from . import utils
from . import JsonTreeParser


def main(
    *,
    input_filepath: str,
    output_filepath: str,
    key: Optional[str],
    tree: Optional[str],
    view: Optional[bool],
) -> Optional[NotImplementedError]:
    file_io = utils.FileIO(src=input_filepath)
    file_data = file_io.load()

    pdt = JsonTreeParser(file_data)

    if key or view:
        pdt_tree = pdt.tree_by_key_or_view(
            key=key,
            view=view,
            result_to=config.Key.SAVE if output_filepath else config.Key.SHOW,
        )
    elif tree:
        pdt_tree = (tree,)
    else:
        raise NotImplementedError("[k]ey or [t]ree or [v]iew is required")

    for tree in pdt_tree:
        if not tree:
            continue

        tree_data = pdt.data_by_tree(tree=tree)

        if output_filepath:
            if output_filepath == config.FD.STDOUT:
                print(tree)
                pprint(tree_data)
                print()
                continue

            if key:
                raise NotImplementedError(
                    "Use `-t` flag to dump a value for `tree`",
                )

            file_io.dump(data=tree_data, dst=output_filepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI tool to view json tree / structure"
    )

    parser.add_argument("-i", type=str, help="[i]nput filepath")
    parser.add_argument("-o", type=str, help="[o]utput filepath")
    parser.add_argument(
        "-v", type=bool, nargs="?", const=True, help="[v]view json tree"
    )
    parser.add_argument("-k", type=str, help="[k]ey to search")
    parser.add_argument("-t", type=str, help="[t]ree to `-o` the data from")
    parser.add_argument("-l", type=int, help="[l]imit stdout")
    parser.add_argument("-il", type=int, help="[i]tems [l]imit stdout")
    parser.add_argument("-fk", type=str, help="[f]ilter stdout by `key`")
    parser.add_argument("-fv", type=str, help="[f]ilter stdout by `value`")
    args = parser.parse_args()

    input_filepath = args.i
    output_filepath = args.o
    key = args.k
    tree = args.t
    view = args.v

    if not input_filepath:
        print("[i]nput filepath is required")
        exit()
    if sum(map(bool, (key, tree, view))) != 1:
        print("Only one of [k]ey or [t]ree or [v]iew is required!")
        exit()

    if args.l:
        # decrements the limit befor returning the `tree`
        config.Tree.SEARCH_LIMIT = args.l + 1
    if args.il:
        config.Tree.SEARCH_ITEMS_LIMIT = args.il

    if args.fk:
        config.Tree.SEARCH_FILTER_KEY = args.fk
    if args.fv:
        config.Tree.SEARCH_FILTER_VALUE = args.fv

    main(
        input_filepath=input_filepath,
        output_filepath=output_filepath,
        key=key,
        tree=tree,
        view=view,
    )
