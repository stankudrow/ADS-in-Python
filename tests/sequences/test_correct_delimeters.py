#!/usr/bin/env python3
"""Tests for the `Match opening-closing delimeters` problem."""


from typing import Sequence

from pytest import mark, raises

from adspy.sequences.correct_delimeters import (
    is_correct_delimeters,
    is_correct_sequence,
)


LDS = "({[<"
RDS = ")}]>"


@mark.parametrize(
    "seq1, seq2, res",
    [
        ("<", ">", True),
        ("{", "]", True),
        ("(", "}}", False),
        ("}", "}", False),
    ],
)
def test_match_delimeters(
    seq1: Sequence, seq2: Sequence, res: bool
):
    """Tests delimeter sequences to be correct."""
    assert is_correct_delimeters(seq1, seq2) is res


@mark.parametrize(
    "seq, res",
    [
        ([], True),
        ("()", True),
        ("(){}[]<>", True),
        ("(<[{}]>)", True),
        (")(", False),
        ("<>]", False),
        ("<", False),
    ],
)
def test_match_sequences(seq: Sequence, res: bool):
    """Tests sequences on correctness."""
    assert is_correct_sequence(seq, lefty=LDS, righty=RDS) is res


def test_match_sequences_exception():
    """Bad delimeters should raise ValueError."""
    seq = "()"
    with raises(ValueError):
        is_correct_sequence(seq, LDS, LDS)
    with raises(ValueError):
        is_correct_sequence(seq, LDS, RDS[:-2])
