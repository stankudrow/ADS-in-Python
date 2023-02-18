#!/usr/bin/env python3
"""The tests on binary search algorithm implementations."""


from typing import Any, List, Sequence, Tuple

from adspy.searching.linear_search import (
    linsearch_iterative,
    linsearch_recursive,
)

from .preconf import (
    BASIC_ITERS_ELEMS_INDICES,
    mark,
)

ARGS = BASIC_ITERS_ELEMS_INDICES


@mark.parametrize("seq, items_results", ARGS)
def test_linear_search(
    seq: Sequence[Any], items_results: List[Tuple[Any, Any]]
):
    """Tests linear search implementations."""
    for item, result in items_results:
        assert (
            linsearch_iterative(seq, item)
            == linsearch_recursive(seq, item)
            == result
        )
