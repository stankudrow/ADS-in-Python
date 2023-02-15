#!/usr/bin/env python3
"""Tests the factorise function."""


from pytest import mark, param

from adspy.math.factorise import factorise


@mark.parametrize(
    "number, factors",
    [
        param(4.2, [], marks=mark.xfail(reason="float")),
        param(-1, [], marks=mark.xfail(reason="<0")),
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (5, [5]),
        (6, [2, 3]),
        (7, [7]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (10, [2, 5]),
        (11, [11]),
        (12, [2, 2, 3]),
        (18, [2, 3, 3]),
    ],
)
def test_is_prime(number: int, factors: list[int]):
    """Tests the factorise function."""
    print(f"num = {number}")
    assert factorise(number) == factors
