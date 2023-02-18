#!/usr/bin/env python3
"""The tests on binary search algorithm implementations."""


from typing import Any, List, Sequence, Tuple

import pytest

from adspy.searching.binary_search import (
    binsearch_iterative,
    binsearch_recursive,
)

from .preconf import (
    BASIC_ITERS_ELEMS_INDICES,
    mark,
    param,
)

BIN_SEARCH_SPECIFIC_ARGS = [
    param(
        [5, 2, 7],
        [
            (2, 1),  # OK
            (5, 0),  # Not OK
        ],
        marks=mark.xfail(reason="Not a sorted sequence."),
    ),
]

ARGS = BASIC_ITERS_ELEMS_INDICES + BIN_SEARCH_SPECIFIC_ARGS


@pytest.mark.parametrize(
    "seq, items_results",
    ARGS
)
def test_binary_search(
    seq: Sequence[Any], items_results: List[Tuple[Any, Any]]
):
    """Tests binary search implementations."""
    for item, result in items_results:
        assert (
            binsearch_iterative(seq, item)
            == binsearch_recursive(seq, item)
            == result
        )
