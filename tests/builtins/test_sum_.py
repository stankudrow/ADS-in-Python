#!/usr/bin/env python3
"""The sum_() test suite."""


from typing import Sequence

from pytest import mark

from adspy.builtins.sum_ import (
    sum_iterative,
    sum_recursive,
)


@mark.parametrize(
    "seq",
    [
        [],
        [0],
        [1],
        [-1, 2],
        range(-10, 11),
    ],
)
def test_sum(seq: Sequence):
    """test_sum"""
    assert sum_recursive(seq) == sum_iterative(seq) == sum(seq)
