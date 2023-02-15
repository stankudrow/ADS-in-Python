#!/usr/bin/env python3
"""The tests on the Flood Fill algorithm."""


from pytest import mark, param

from adspy.flooding.flood_fill import (
    flood_fill_recursive as ffrec,
)


@mark.parametrize(
    "screen, ycoord, xcoord, newval, result",
    [
        ([], 0, 0, "x", []),
        ([], 1, 1, "x", []),
        ([["x"]], 0, 0, "o", [["o"]]),
        ([["x", "x"]], 0, 1, "o", [["o", "o"]]),
        ([["x", "x"]], 0, 1, "x", [["x", "x"]]),
        ([["x", "o", "x"]], 0, 1, "t", [["x", "t", "x"]]),
        (
            [["x", "o"], ["o", "x"]],
            1,
            0,
            "?",
            [["x", "o"], ["?", "x"]],
        ),
        (
            [["x", "o", "x"], ["#", "o", "?"], ["o", "o", "o"]],
            2,
            1,
            "Z",
            [["x", "Z", "x"], ["#", "Z", "?"], ["Z", "Z", "Z"]],
        ),
        (
            [
                ["o", "x", "o", "o", "?"],
                ["x", "o", "o", "x", "?"],
                ["o", "x", "o", "o", ""],
            ],
            1,
            1,
            "?",
            [
                ["o", "x", "?", "?", "?"],
                ["x", "?", "?", "x", "?"],
                ["o", "x", "?", "?", ""],
            ],
        ),
        param([], -1, 1, "x", [], marks=mark.xfail(reason="at least one negative coord.")),
        param([], 1, -1, "x", [], marks=mark.xfail(reason="at least one negative coord.")),
    ],
)
def test_fllod_fill(screen, ycoord, xcoord, newval, result):
    """Tests the Flood Fill algorithm."""
    ffrec(screen, ycoord, xcoord, newval)
    assert screen == result
