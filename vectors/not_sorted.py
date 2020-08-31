import numpy as np


class NotSortedVector:
    def __init__(self, size):
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=int)

    # Big O ---> O(N)
    def print_elements(self):
        if self.last_position == -1:
            print("Vector empty.")
        else:
            for i in range(self.last_position + 1):
                print(f"Position: {i} ---- Value: {self.values[i]}")

    # Big O ---> O(2)
    def insert(self, value):
        if self.last_position == self.size - 1:
            print("Vector full.")
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    # Big O ---> O(N)
    def search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] == value:
                return i
        return None

    # Big O ---> O(N)
    def delete(self, value):
        position = self.search(value)
        if not position:
            return position
        for i in range(position, self.last_position):
            self.values[i] = self.values[i + 1]
        self.last_position -= 1


vector_1 = NotSortedVector(5)

vector_1.print_elements()

vector_1.insert(5)
vector_1.insert(4)
vector_1.insert(1)
vector_1.insert(3)
vector_1.insert(0)

vector_1.print_elements()

print(vector_1.search(4))
print(vector_1.search(1))
print(vector_1.search(2))

vector_1.delete(10)
vector_1.print_elements()
