#!/usr/bin/env python3
"""The abs_() test suite."""


from pytest import mark

from adspy.math.abs import abs_


@mark.parametrize(
    "number",
    [
        -1,
        0,
        1,
        -4.2,
        2.1,
        1 + 1j,
        -1 + 1j,
        -1 + 1j,
        -1 - 1j,
    ],
)
def test_abs(number: int | float | complex):
    """test_abs

    Parameters
    ----------
    number: int | float | complex
    """
    assert abs_(number) == abs(number)
