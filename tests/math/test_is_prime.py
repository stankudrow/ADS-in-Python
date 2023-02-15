#!/usr/bin/env python3
"""Tests the is_prime function."""


from pytest import mark, param

from adspy.math.is_prime import is_prime


@mark.parametrize(
    "number, result",
    [
        param(4.2, False, marks=mark.xfail(reason="float")),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (9, False),
    ],
)
def test_is_prime(number: int, result: bool):
    """Tests the is_prime function."""
    assert is_prime(number) == result
