#!/usr/bin/env python3
"""The function decomposes a number into prime factors."""


from math import sqrt


def factorise(number: int) -> list[int]:
    """Returns the prime factors of the number.

    Parameters
    ----------
    number : int

    Raises
    ------
    TypeError
        if the number if not integer.
    ValueError
        if the number is a negative integer.

    Returns
    -------
    list[int]
    """
    if not isinstance(number, int):
        raise TypeError(f"{number} is not integer")
    if number < 0:
        raise ValueError(f"{number} is negative")
    factors: list[int] = []
    while number and number % 2 == 0:
        factors.append(2)
        number //= 2
    factor: int = 3
    while factor <= int(sqrt(number)):
        while number % factor == 0:
            factors.append(factor)
            number //= factor
        factor += 2
    if number > 1:
        factors.append(number)
    return factors
