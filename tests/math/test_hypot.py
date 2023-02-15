#!/usr/bin/env python3
"""Tsets for the hypotenuse problem."""


from math import hypot, isclose

from pytest import mark

from adspy.math.hypot import hypot_


@mark.parametrize(
    "coords",
    [
        [],
        [0],
        [42],
        [-1, 1],
        [2, 6, 8],
    ],
)
def test_hypot(coords):
    """Tests the multidimentional Euclidean distance (hypotenuse)."""
    assert isclose(hypot_(*coords), hypot(*coords))
