#!/usr/bin/env python3
"""The merge_sort algorithm with merge function."""


from typing import Any, Callable, List, Optional, Sequence

# https://en.wikipedia.org/wiki/Merge_sort


def merge(
    seq1: Sequence,
    seq2: Sequence,
    key: Optional[Callable] = None,
    reverse: bool = False,
) -> List:
    """Returns the list of two iterables merged in a sorted way.

    An auxiliary tool for the merge_sort function.

    Parameters
    ----------
    seq1 : Sequence
    seq1 : Sequence
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
    merged = []
    lst1, lst2 = map(list, (seq1, seq2))
    len1, len2 = map(len, (lst1, lst2))
    idx1, idx2 = 0, 0
    while (idx1 < len1) and (idx2 < len2):
        if key(seq1[idx1]) < key(seq2[idx2]):
            merged.append(seq1[idx1])
            idx1 += 1
        else:
            merged.append(seq2[idx2])
            idx2 += 1
    merged += seq1[idx1:]
    merged += seq2[idx2:]
    if reverse:
        merged.reverse()
    return merged


def merge_sort(
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

    def merge_sort_rec(
        lst: List,
        key: Optional[Callable] = None,
        reverse: bool = False,
    ) -> List:
        """The actual recursive implementation."""
        size = len(lst)
        if size < 2:
            return lst
        mid = size // 2
        left_half = merge_sort_rec(lst[:mid], key, reverse)
        right_half = merge_sort_rec(lst[mid:], key, reverse)
        return merge(left_half, right_half, key, reverse)

    sorted_lst = merge_sort_rec(
        list(seq), key=key, reverse=False
    )
    if reverse:
        sorted_lst.reverse()
    return sorted_lst
