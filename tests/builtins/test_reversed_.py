#!/usr/bin/env python3
"""The tests on sequence reversion implementations."""


from typing import Sequence

from pytest import mark, param

from adspy.builtins.reversed_ import (
    reversed_iterative,
    reversed_recursive,
)

from ..results import Result


@mark.parametrize(
    "seq",
    [
        "",
        "1",
        "ab",
        "1d2c",
        [1, "2", (3, 4)],
        range(5),
        param(
            (i for i in range(5)),
            marks=mark.xfail(reason="Generator"),
        ),
    ],
)
def test_reversed(seq: Sequence):
    """test_reversed implementations."""
    results = map(
        list,
        map(
            lambda fut: fut.result(),
            [
                Result(reversed_iterative, seq),
                Result(reversed_recursive, seq),
            ],
        ),
    )
    expected = list(seq)[::-1]
    for result in results:
        assert result == expected
