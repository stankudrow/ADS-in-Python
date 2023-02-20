#!/usr/bin/env python3
"""Detects if a sequence is "palindromic"."""


from typing import Sequence


def is_palindrome_recursive(seq: Sequence) -> bool:
    """Returns True if the sequence is a palindrome.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    bool
    """
    if len(seq) < 2:
        return True
    if seq[0] != seq[-1]:
        return False
    return is_palindrome_recursive(seq[1:-1])


def is_palindrome_iterative(seq: Sequence) -> bool:
    """Returns True if the sequence is a palindrome.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    bool
    """
    length: int = len(seq)
    if length < 2:
        return True
    for index in range(length // 2):
        if seq[index] != seq[-(index + 1)]:
            return False
    return True
