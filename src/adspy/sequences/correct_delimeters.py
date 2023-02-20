#!/usr/bin/env python3
"""The `Match opening-closing delimeters` problem."""


from typing import Sequence

from adspy.data_structures.stack import Stack


def is_correct_delimeters(
    lefty: Sequence,
    righty: Sequence,
) -> bool:
    """Evaluates sequences to be correct left-right delimeter sequences.

    Two sequences are correct left-right delimeters if:
        * their lengths are equal;
        * they have no common elements.

    Parameters
    ----------
    lefty : Sequence
        delimeters from the left
    righty : Sequence
        delimeters from the right

    Raises
    ------
    bool
    """
    if len(lefty) != len(righty):
        return False
    if set(lefty) & set(righty):
        return False
    return True


def is_correct_sequence(
    seq: Sequence,
    lefty: Sequence,
    righty: Sequence,
) -> bool:
    """Matches the sequence of delimiters to form a correct sequence.

    Parameters
    ----------
    seq: Sequence,
    lefty: Sequence
    righty: Sequence

    Raises
    ------
    ValueError
        If delimeters are not correct sequences.
        See `is_correct_delimeters` function.

    Returns
    -------
    bool
    """
    if not is_correct_delimeters(lefty, righty):
        raise ValueError("bad delimeters")
    stack = Stack()
    for item in seq:
        if item in lefty:
            stack.push(item)
        if item in righty:
            if not stack:
                return False
            if lefty.index(stack.pop()) != righty.index(item):
                return False
    return not stack  # if is empty
