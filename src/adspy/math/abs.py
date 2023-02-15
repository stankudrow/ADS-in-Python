#!/usr/bin/env python3
"""The abs() builtin function."""


from math import hypot  # see math algorithms


def abs_(number: int | float | complex) -> int | float:
    """Returns the absolute value of the argument.

    Parameters
    ----------
    number : int | float | complex
        the argument.

    Returns
    -------
    int | float
        the absolute value of the argument (number).
    """
    if isinstance(number, complex):
        return hypot(number.real, number.imag)
    return -number if number < 0 else number
