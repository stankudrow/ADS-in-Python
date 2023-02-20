#!/usr/bin/env python3
"""
The Queue First-In-First-Out (FIFO) data structure.
"""


from typing import Any, Optional, Sequence


class QueueError(Exception):
    """Generic Queue Exception."""


class Queue:
    """The Queue data structure."""

    def __init__(
        self,
        seq: Optional[Sequence] = None,
        maxlen: Optional[int] = None,
    ):
        self._queue = [] if seq is None else list(seq)
        if maxlen and maxlen < 0:
            raise QueueError(f"maxlen (={maxlen}) < 0")
        self._maxlen = maxlen
        self._head = 0

    def __bool__(self) -> bool:
        return bool(len(self))

    def __len__(self) -> int:
        return (
            len(self._queue[self._head :]) if self._queue else 0
        )

    def __repr__(self) -> str:
        return f"Queue({self._queue})"

    def _squeeze(self):
        """Reduces the size of the queue after excedding the half of the queue."""
        if self._head > len(self) // 2:
            self._queue = self._queue[self._head :]
            self._head = 0

    def clear(self):
        """Clears the queue, making it empty."""
        self._queue.clear()
        self._head = 0

    def is_empty(self) -> bool:
        """Returns True if the queue is empty."""
        return not bool(self)

    def extend(self, seq: Sequence):
        """Pushes the elements from the sequence."""
        self._squeeze()
        lst = list(seq)
        if self.maxlen is None:
            cap = len(lst)
        else:
            cap = min(len(lst), self.maxlen - len(self))
        for idx in range(cap):
            self._queue.append(lst[idx])

    def dequeue(self) -> Any:
        """Pops the first/front element.

        Raises
        ------
        IndexError
            if empty.
        """
        item = self._queue[self._head]
        self._head += 1
        self._squeeze()
        return item

    def enqueue(self, value: Any):
        """Pushes the value into the queue."""
        if self.maxlen is None or (
            (self.maxlen is not None) and len(self) < self.maxlen
        ):
            self._queue.append(value)
        else:
            raise QueueError(
                f"cannot exceed maxlen ({self.maxlen})"
            )

    @property
    def front(self) -> Any:
        """Returns the first/front element of the queue.

        Raises
        ------
        IndexError
            if empty.
        """
        return self._queue[self._head]

    @property
    def maxlen(self) -> Optional[int]:
        """Returns the maximum length of the stack."""
        return self._maxlen
