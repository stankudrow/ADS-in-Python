#!/usr/bin/env python3
"""The Stack data structure test suite."""


from typing import List, Sequence

from pytest import fixture, mark, raises

from adspy.data_structures.stack import Stack


# https://miguendes.me/how-to-use-fixtures-as-arguments-in-pytestmarkparametrize
# https://stackoverflow.com/questions/46089480/pytest-fixtures-redefining-name-from-outer-scope-pylint


@fixture(scope="module", name="seqs")
def sequences() -> List[Sequence]:
    """Test sequences for the Stack DS."""
    return [
        [],
        (-1, 1),
        "abc",
    ]


@fixture(scope="module", name="args")
def init_args(seqs) -> List[Sequence]:
    """Test arguments for the Stack.__init__()."""
    return [None] + seqs


class TestStack:
    """The Stack test suite."""

    @mark.parametrize("arg", ["args"])
    def test_init(self, arg, request):
        """Tests self.__init__()."""
        value = request.getfixturevalue(arg)
        assert Stack(value) is not None

    @mark.parametrize("arg", ["args"])
    def test_len(self, arg, request):
        """Tests self.__len__()."""
        value = request.getfixturevalue(arg)
        stack = Stack(value)
        if value is None:
            value = []
        assert len(stack) == len(value)

    @mark.parametrize("arg", ["seqs"])
    def test_push(self, arg, request):
        """Tests self.push(item)."""
        stack = Stack()
        for seq in request.getfixturevalue(arg):
            for val in seq:
                stack.push(val)
                assert stack.top == val

    @mark.parametrize(
        "seq",
        [
            [],
            [1],
        ],
    )
    def test_pop(self, seq):
        """Tests self.pop()."""
        stack = Stack(seq)
        if seq:
            assert stack.pop() == seq[-1]
        else:
            with raises(IndexError):
                stack.pop()
            with raises(IndexError):
                stack.top  # pylint: disable=pointless-statement

    def test_bool(self):
        """Tests self.__bool__()."""
        stack = Stack()
        assert bool(stack) is False
        stack.push(5)
        assert bool(stack) is True
        stack.pop()
        assert bool(stack) is False

    @mark.parametrize("arg", ["seqs"])
    def test_extend(self, arg, request):
        """Tests self.extend(seq)."""
        stack = Stack()
        for seq in request.getfixturevalue(arg):
            stack.extend(seq)
            for item in reversed(seq):
                assert stack.pop() == item

    @mark.parametrize("arg", ["seqs"])
    def test_clear(self, arg):
        """Tests self.clear()."""
        stack = Stack(arg)
        stack.clear()
        assert len(stack) == 0

    @mark.parametrize("arg", ["seqs"])
    def test_is_empty(self, arg, request):
        """Tests self.is_empty()."""
        stack = Stack()
        for seq in request.getfixturevalue(arg):
            stack.extend(seq)
            for item in reversed(seq):
                assert stack.pop() == item
