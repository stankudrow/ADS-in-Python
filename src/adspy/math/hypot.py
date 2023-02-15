#!/usr/bin/env python3
"""The multidimentional Euclidean distance (hypotenuse) problem."""


from math import sqrt  # see math algorithms


def hypot_(*coords) -> int | float:
    """Computes the multidimentional Euclidean distance.

    The distance is computed from the origin to a point.

    Parameters
    ----------
    coords : the tuple of points (coordinates)

    Returns
    -------
    int | float
        the hypotenuse of the coordinates.
    ."""
    return sqrt(sum(coord**2 for coord in coords))
