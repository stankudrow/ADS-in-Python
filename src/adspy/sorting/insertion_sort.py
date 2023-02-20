#!/usr/bin/env python3
"""The insertion_sort algorithm."""


from typing import Any, Callable, List, Optional, Sequence

# https://en.wikipedia.org/wiki/Insertion_sort


def insertion_sort(
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
    for idx in range(1, len(lst)):
        curr = lst[idx]
        jdx = idx - 1
        while jdx > -1 and key(lst[jdx]) > key(lst[jdx + 1]):
            lst[jdx + 1], lst[jdx] = lst[jdx], lst[jdx + 1]
            jdx -= 1
        lst[jdx + 1] = curr
    if reverse:
        lst.reverse()
    return lst
