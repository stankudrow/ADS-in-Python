#!/usr/bin/env python3
"""Tests on palindrome detection."""


from typing import Sequence

from pytest import mark

from adspy.sequences.is_palindrome import (
    is_palindrome_iterative,
    is_palindrome_recursive,
)


@mark.parametrize(
    "seq, res",
    [
        ("", True),
        ("1", True),
        ("11", True),
        ("121", True),
        ("32123", True),
        ("12", False),
        ("1234", False),
    ],
)
def test_is_palindrome(seq: Sequence, res: bool):
    """test_is_palindrome.

    Parameters
    ----------
    seq : Sequence
    """
    assert (
        is_palindrome_recursive(seq)
        == is_palindrome_iterative(seq)
        == res
    )
