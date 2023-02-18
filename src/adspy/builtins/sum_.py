#!/usr/bin/env python3
"""The sum() builtin function."""


from typing import Iterable


def sum_iterative(iterable: Iterable, start: int = 0) -> int:
    """Returns the sum of the elements from the iterable.

    Parameters
    ----------
    iterable : Iterable
        with __add__ protocol.
    start : int, default 0
        the initial value that is an offset to the sum.

    Returns
    -------
    int
    """
    summa: int = start
    for elem in iterable:
        summa += elem
    return summa


def sum_recursive(iterable: Iterable, start: int = 0) -> int:
    """Returns the sum of the elements from the iterable.

    Parameters
    ----------
    iterable : Iterable
        with __add__ protocol.
    start : int, default 0
        the initial value that is an offset to the sum.

    Returns
    -------
    int
    """

    def sum_rec(iter_: Iterable) -> int:
        """Returns the sum of the elements of the iterable."""
        try:
            elem = next(iter_)
        except StopIteration:
            return 0
        return elem + sum_rec(iter_)

    iterator = iter(iterable)
    return start + sum_rec(iterator)
