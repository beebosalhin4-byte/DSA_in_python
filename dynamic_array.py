"""Generic DynamicArray for DSA_in_python

Translated from Java implementation to a Python generic implementation.
Uses a Python list as backing storage with explicit capacity and length to
mirror the original behavior while keeping it Pythonic.
"""
from typing import Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class DynamicArray(Generic[T]):
    """A simple generic dynamic array.

    Notes:
    - Backed by a Python list pre-filled with None to represent capacity.
    - capacity doubles when more space is needed.
    - remove_at does not automatically shrink capacity; it simply shifts
      elements left and clears the freed slot. This is more efficient than
      allocating a brand new backing array on every removal (the original
      Java example recreated the backing array on removeAt).
    """

    def __init__(self, capacity: int = 16) -> None:
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}")
        self.capacity: int = capacity
        self.arr: List[Optional[T]] = [None] * self.capacity
        self.len: int = 0

    def size(self) -> int:
        return self.len

    def is_empty(self) -> bool:
        return self.len == 0

    def get(self, index: int) -> T:
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        # type: ignore[return-value]
        return self.arr[index]

    def set(self, index: int, elem: T) -> None:
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        self.arr[index] = elem

    def clear(self) -> None:
        for i in range(self.len):
            self.arr[i] = None
        self.len = 0

    def _grow(self) -> None:
        old_cap = self.capacity
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= 2
        self.arr.extend([None] * (self.capacity - old_cap))

    def add(self, elem: T) -> None:
        if self.len + 1 >= self.capacity:
            self._grow()
        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, rm_index: int) -> T:
        if rm_index < 0 or rm_index >= self.len:
            raise IndexError("Index out of bounds")
        # type: ignore[var-annotated]
        data: T = self.arr[rm_index]  # stored value to return
        # shift elements left
        for i in range(rm_index, self.len - 1):
            self.arr[i] = self.arr[i + 1]
        # clear the now-unused slot
        self.len -= 1
        self.arr[self.len] = None
        return data

    def remove(self, obj: object) -> bool:
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True

    def index_of(self, obj: object) -> int:
        for i in range(self.len):
            if obj is None:
                if self.arr[i] is None:
                    return i
            else:
                if obj == self.arr[i]:
                    return i
        return -1

    def contains(self, obj: object) -> bool:
        return self.index_of(obj) != -1

    def __iter__(self) -> Iterator[T]:
        for i in range(self.len):
            # type: ignore[yield-value]
            yield self.arr[i]

    def __str__(self) -> str:
        if self.len == 0:
            return "[]"
        return "[" + ", ".join(str(self.arr[i]) for i in range(self.len)) + "]"


if __name__ == "__main__":
    # small demo
    da = DynamicArray[int]()
    da.add(3)
    da.add(7)
    da.add(6)
    da.add(-2)

    print(da)  # -> [3, 7, 6, -2]
    da.remove(6)
    print(da)  # -> [3, 7, -2]
    print(da.contains(7))  # -> True
    print(da.index_of(100))  # -> -1
