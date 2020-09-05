import numpy as np


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

    # [1, 2, 2, 2, 4, 5, 7]
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
vector_1.insert(8)
vector_1.insert(1)
vector_1.insert(50)
vector_1.print_elements()
vector_1.delete(1)
vector_1.print_elements()