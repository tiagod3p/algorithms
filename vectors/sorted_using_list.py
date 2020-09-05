from math import ceil


def insert(list_of_numbers: list, value: int):
    position = 0
    length = len(list_of_numbers)
    for i in range(length):
        position = i
        if list_of_numbers[i] > value:
            break
        if position == length - 1:
            position += 1

    list_of_numbers.append(None)
    while length >= position:
        length -= 1
        list_of_numbers[length + 1] = list_of_numbers[length]

    list_of_numbers[position] = value
    return list_of_numbers


def binary_search(list_of_numbers: list, value: int):
    initial = 0
    last = len(list_of_numbers) - 1
    while True:
        current = ceil((initial + last) / 2)
        if initial > last:
            return None
        if list_of_numbers[current] == value:
            return current
        if list_of_numbers[current] > value:
            last = current - 1
        else:
            initial = current + 1


list_of_numbers = [1, 2, 4, 8, 9, 10, 11, 25, 28]

insert(list_of_numbers, 12)
insert(list_of_numbers, 15)
insert(list_of_numbers, 12)
insert(list_of_numbers, 11)
insert(list_of_numbers, 13)
insert(list_of_numbers, 25)
insert(list_of_numbers, 29)
insert(list_of_numbers, 30)
insert(list_of_numbers, 42)
insert(list_of_numbers, 26)
print(list_of_numbers)
