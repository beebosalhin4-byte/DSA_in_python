class IntArray:
    _DEFAULT_CAP = 1 << 3  # 8

    def __init__(self, initial_input=None):
        # Handle the default constructor: IntArray()
        if initial_input is None:
            self.capacity = self._DEFAULT_CAP
            self.len = 0
            self.arr = [0] * self.capacity

        # Handle the array constructor: IntArray(int[] array)
        elif isinstance(initial_input, list):
            self.arr = list(initial_input)
            self.capacity = len(initial_input)
            self.len = len(initial_input)

        # Handle the capacity constructor: IntArray(int capacity)
        elif isinstance(initial_input, int):
            if initial_input < 0:
                raise ValueError(f"Illegal Capacity: {initial_input}")
            self.capacity = initial_input
            self.len = 0
            self.arr = [0] * self.capacity
            
        else:
            raise TypeError("Invalid argument type")

    def size(self):
        return self.len

    def __iter__(self):
        # Implements the Iterable interface logic for Python
        for i in range(self.len):
            yield self.arr[i]

"""Arrays utilities for DSA_in_python

Translated IntArray dynamic array from Java to Python and adjusted behavior to be Pythonic.
"""
from bisect import bisect_left
from typing import Iterator, List


class IntArray:
    """A simple dynamic array for integers mimicking the Java IntArray example.

    Under the hood this uses a Python list as backing storage and manages
    an explicit capacity and length to mirror the original implementation.
    """

    def __init__(self, capacity: int = 0) -> None:
        self.capacity: int = max(0, capacity)
        self.arr: List[int] = [0] * self.capacity
        self.len: int = 0

    def size(self) -> int:
        return self.len

    def __len__(self) -> int:
        return self.len

    def is_empty(self) -> bool:
        return self.len == 0

    # Direct access: array.arr[index]
    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        return self.arr[index]

    def set(self, index: int, elem: int) -> None:
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        self.arr[index] = elem

    def _grow(self) -> None:
        old_cap = self.capacity
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= 2
        self.arr.extend([0] * (self.capacity - old_cap))

    def add(self, elem: int) -> None:
        if self.len + 1 >= self.capacity:
            self._grow()
        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, rm_index: int) -> None:
        if rm_index < 0 or rm_index >= self.len:
            raise IndexError("Index out of bounds")
        # shift elements left
        for i in range(rm_index, self.len - 1):
            self.arr[i] = self.arr[i + 1]
        self.len -= 1
        # Optional: clear the freed slot for clarity
        if self.len < len(self.arr):
            self.arr[self.len] = 0
        # Note: we do not automatically shrink capacity here. If desired,
        # a shrink policy can be implemented (e.g., halve capacity when len <= capacity // 4).

    def remove(self, elem: int) -> bool:
        for i in range(self.len):
            if self.arr[i] == elem:
                self.remove_at(i)
                return True
        return False

    def reverse(self) -> None:
        for i in range(self.len // 2):
            j = self.len - i - 1
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def binary_search(self, key: int) -> int:
        """Mimic java.util.Arrays.binarySearch return value.

        Returns index >= 0 if found; if not found returns -(insertion_point) - 1
        where insertion_point is the index at which the key would be inserted to keep
        the array sorted.
        """
        # operate only on the active portion
        lo = 0
        hi = self.len
        # use bisect_left to find potential insertion point
        i = bisect_left(self.arr, key, lo, hi)
        if i != self.len and self.arr[i] == key:
            return i
        return -i - 1

    def sort(self) -> None:
        # sort only the active portion
        sorted_part = sorted(self.arr[: self.len])
        self.arr[: self.len] = sorted_part

    def __iter__(self) -> Iterator[int]:
        for i in range(self.len):
            yield self.arr[i]

    def __str__(self) -> str:
        if self.len == 0:
            return "[]"
        return "[" + ", ".join(str(self.arr[i]) for i in range(self.len)) + "]"


if __name__ == "__main__":
    ar = IntArray(50)
    ar.add(3)
    ar.add(7)
    ar.add(6)
    ar.add(-2)

    ar.sort()  # [-2, 3, 6, 7]

    # Prints each element on its own line: -2 3 6 7
    for i in range(ar.size()):
        print(ar.get(i))

    # Prints the whole array: [-2, 3, 6, 7]
    print(ar)
