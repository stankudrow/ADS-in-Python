#!/usr/bin/env python3
"""The reversed() builtin function."""


from typing import Generator, Iterator, Sequence


def reversed_iterative(sequence: Sequence) -> Generator:
    """Reverses (iteratively) the sequence."""
    for idx in range(len(sequence) - 1, -1, -1):
        yield sequence[idx]


def reversed_recursive(sequence: Sequence) -> Generator:
    """Reverses (recursively) the sequence."""

    def rev_rec(seq: Sequence, last: int):
        """Returns the reversed iterator of the sequence."""
        if last == 0:
            return
        last -= 1
        yield seq[last]
        yield from rev_rec(seq, last)

    yield from rev_rec(sequence, len(sequence))
