#!/usr/bin/env python3
"""The tests on sequence reversion implementations."""


from typing import Callable, List, Sequence

from pytest import fixture, mark, param

from adspy.builtins.reversed_ import (
    reversed_iterative,
    reversed_recursive,
)


class Result:
    """A Future-like interface."""

    def __init__(self, func: Callable, /, *args, **kwargs):
        try:
            self._result = func(*args, **kwargs)
        except BaseException as bexc:
            self._result = bexc

    def result(self):
        """May return the result."""
        if isinstance(self._result, BaseException):
            raise self._result
        return self._result


@fixture(scope="module", name="seqs")
def sequences() -> List[Sequence]:
    """Samples."""
    return [
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
    ]


@mark.parametrize("seq", ["seqs"])
def test_reversed(seq: Sequence):
    """test_reversed implementations."""
    results = list(
        map(
            list,
            map(
                lambda fut: fut.result(),
                [
                    Result(reversed_iterative, seq),
                    Result(reversed_recursive, seq),
                ],
            ),
        )
    )
    expected = list(seq)[::-1]
    for result in results:
        assert result == expected
