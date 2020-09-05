import numpy as np
from math import ceil


class SortedVector:
    def __init__(self, size):
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=int)

    def print_elements(self):
        if self.last_position == -1:
            print("Vector empty.")
        else:
            for i in range(self.last_position + 1):
                print(f"Position: {i} ---- Value: {self.values[i]}")

    # Big O ---> O(N)
    def insert(self, value):
        if self.last_position + 1 == self.size:
            print("Vector full.")
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if position == self.last_position:
                position = i + 1

        j = self.last_position
        while j >= position:
            self.values[j + 1] = self.values[j]
            j -= 1

        self.values[position] = value
        self.last_position += 1

    # Big O ---> O(N)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return None
            if self.values[i] == value:
                return i
        return None

    # Big O ---> O(logN)
    def binary_search(self, value):
        initial_position = 0
        last_position = self.last_position

        while True:
            current_position = ceil((initial_position + last_position) / 2)
            if initial_position > last_position:
                return None
            if self.values[current_position] == value:
                return current_position
            if self.values[current_position] > value:
                last_position = current_position - 1
            else:
                initial_position = current_position + 1

    # Big O ---> O(N)
    def delete(self, value):
        position = self.linear_search(value)
        if position is None:
            return position
        for i in range(position, self.last_position):
            self.values[i] = self.values[i + 1]
        self.last_position -= 1


vector_1 = SortedVector(5)
vector_1.print_elements()
vector_1.insert(10)
vector_1.insert(7)
vector_1.insert(9)
vector_1.insert(1)
vector_1.insert(50)
vector_1.print_elements()
print(vector_1.binary_search(8))
