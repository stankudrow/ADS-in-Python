#!/usr/bin/env python3
"""The bubble_sort algorithm."""


from typing import Any, Callable, List, Optional, Sequence

# https://en.wikipedia.org/wiki/Bubble_sort


def bubble_sort(
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
    while True:
        swapped = False
        for idx in range(1, size):
            if key(lst[idx - 1]) > key(lst[idx]):
                lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
                swapped = True
        if not swapped:
            break
        size -= 1
    if reverse:
        lst.reverse()
    return lst
