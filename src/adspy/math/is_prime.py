#!/usr/bin/env python3
"""The is_prime function tests a number on primality."""


from math import sqrt


def is_prime(number: int) -> bool:
    """Returns True if the number is an integer prime one.

    Parameters
    ----------
    number : int

    Raises
    ------
    TypeError
        if the number if not integer.

    Returns
    -------
    bool
    """
    if not isinstance(number, int):
        raise TypeError(f"{number} is not integer")
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for num in range(3, int(sqrt(number)) + 1, 2):
        if number % num == 0:
            return False
    return True
