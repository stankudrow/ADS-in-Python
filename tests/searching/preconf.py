#!/usr/bin/env python3


from pytest import mark, param


BASIC_ITERS_ELEMS_INDICES = [
    param(
        None,
        [(None, None)],
        marks=mark.xfail(reason="None taken in."),
    ),
    param(
        5,
        [(5, 5)],
        marks=mark.xfail(reason="Not a sequence."),
    ),
    ("", [("", None)]),
    ("1", [("1", 0), ("2", None)]),
    ("abc", [("a", 0), ("b", 1), ("c", 2)]),
    ("defG", [("d", 0), ("e", 1), ("f", 2), ("g", None)]),
]
