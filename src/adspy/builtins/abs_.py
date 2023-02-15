#!/usr/bin/env python3
"""The abs() builtin function."""


from numbers import Number


def abs_(obj) -> Number:
    """Returns the absolute value of the object.

    Parameters
    ----------
    obj : object with __abs__ defined dunder.

    Returns
    -------
    Number
        the absolute value of the argument (number).
    """
    return (
        obj.__abs__()
    )  # pylint: disable=unnecessary-dunder-call
