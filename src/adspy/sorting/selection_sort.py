#!/usr/bin/env python3
"""The selection_sort algorithm."""


from typing import Any, Callable, List, Optional, Sequence

# https://en.wikipedia.org/wiki/Selection_sort


def selection_sort(
    seq: Sequence,
    key: Optional[Callable] = None,
    reverse: bool = False,
) -> List:
    """Returns the sorted list.

    Parameters
    ----------
    seq : Sequence
    key : Optional[Callable], default None
    reverse : bool, default False

    Returns
    -------
    List
    """

    def defkey(arg) -> Any:
        """Default key callable value."""
        return arg

    if key is None:
        key = defkey
    lst = list(seq)
    size = len(lst)
    for idx in range(size):
        imin = idx
        for jdx in range(idx + 1, size):
            if key(lst[jdx]) < key(lst[imin]):
                imin = jdx
        if imin != idx:
            lst[idx], lst[imin] = lst[imin], lst[idx]

    if reverse:
        lst.reverse()
    return lst
