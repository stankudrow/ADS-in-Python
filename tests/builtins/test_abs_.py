#!/usr/bin/env python3
"""The abs_() test suite."""


from pytest import mark

from adspy.builtins.abs_ import abs_


class AbsEntity:
    """The class implementing __abs__ method."""

    def __abs__(self) -> int:
        return 42


@mark.parametrize(
    "obj",
    [
        -1,
        0,
        1,
        -4.2,
        2.1,
        1 + 1j,
        -1 + 1j,
        1 - 1j,
        -1 - 1j,
        AbsEntity(),
    ],
)
def test_abs(obj):
    """test_abs_ builtin

    Parameters
    ----------
    number: int | float | complex
    """
    assert abs_(obj) == abs(obj)
