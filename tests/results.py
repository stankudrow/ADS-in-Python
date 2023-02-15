#!/usr/bin/env python3
"""Helper tools for extracting results."""


class Result:
    """A Future-like interface."""

    def __init__(self, func, /, *args, **kwargs):
        try:
            self._result = func(*args, **kwargs)
        except BaseException as bexc:
            self._result = bexc

    def result(self):
        """May return the result."""
        if isinstance(self._result, BaseException):
            raise self._result
        return self._result
