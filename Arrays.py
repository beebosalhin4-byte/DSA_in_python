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
