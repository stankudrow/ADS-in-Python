#!/usr/bin/env python3
"""The test suite on factorials."""


from concurrent.futures import ProcessPoolExecutor, as_completed
from pytest import mark, param

from adspy.math.factorial import (
    factorial_iterative,
    factorial_recursive,
)


@mark.parametrize(
    "nbr, expected",
    [
        param(
            -1, ValueError, marks=mark.xfail(reason="negative")
        ),
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
    ],
)
def test_factorial(nbr: int, expected: int):
    """test_factorial implementations."""
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(factorial_iterative, nbr),
            executor.submit(factorial_recursive, nbr),
        ]
    for fut in as_completed(futures):
        assert fut.result() == expected
