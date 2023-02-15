#!/usr/bin/env python3
"""The test suite on factorials."""


from pytest import mark, param

from adspy.math.factorial import (
    factorial_iterative,
    factorial_recursive,
)


from ..results import Result


@mark.parametrize(
    "nbr, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        param(
            -1, ValueError, marks=mark.xfail(reason="negative")
        ),
    ],
)
def test_factorial(nbr: int, expected: int):
    """test_factorial implementations."""
    futures = [
        Result(factorial_iterative, nbr),
        Result(factorial_recursive, nbr),
    ]
    for fut in futures:
        assert fut.result() == expected
