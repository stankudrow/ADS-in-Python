#!/usr/bin/env python3
"""Tests of implementations of the insertion_sort algorithm."""


from operator import itemgetter
from typing import Callable, Optional, Sequence

from pytest import mark, param

from adspy.sorting.insertion_sort import insertion_sort

# https://en.wikipedia.org/wiki/Sorting_algorithm


@mark.parametrize(
    "seq, key, reverse",
    [
        ([], None, False),
        ([1], None, False),
        ([2, 1], None, False),
        param(
            (1, 0, -1),
            None,
            True,
            marks=mark.xfail(reason="unstable"),
        ),
        param(
            (-7, 5, 2, -5),
            None,
            False,
            marks=mark.xfail(reason="unstable"),
        ),
        (
            [(2, 1), (3, 4), (5, -5), (0, 2)],
            itemgetter(-1),
            True,
        ),
        param(
            [-2, 2, 1, 0, -1],
            abs,
            False,
            marks=mark.xfail(reason="mutual ambiguity"),
        ),
    ],
)
def test_insertion_sort(
    seq: Sequence, key: Optional[Callable], reverse: bool
):
    """Tests the insertion_sort algorithm."""
    lst = list(seq)
    assert insertion_sort(
        lst, key=key, reverse=reverse
    ) == sorted(lst, key=key, reverse=reverse)
