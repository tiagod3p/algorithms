list_1 = [1, 2, 3, 4, 5]


# O(1) - Constant
def constant(n: list):
    return n[0]


# O(N) - Linear
def linear(n: list):
    for i in range(len(n)):
        print(i)


# O(N^c) - Exponential
def exponential(n: list):
    for i in range(len(n)):
        for j in range(len(n)):
            print(i, j)


# Combination -
# O(3) + O(10) + O(N) + O(N) + O(1) = O(14) + O(2N) = O(N),
# constant and multiplication in N we desconsider because N could be
# a number a lot more bigger
def combination(n: list):
    # O(3)
    print(n[0])
    print(n[1])
    print(n[2])

    # O(10)
    for i in range(10):
        print(i)

    # O(N)
    for j in range(len(n)):
        print(j)

    # O(N)
    for k in range(len(n)):
        print(k)

    # O(1)
    print('test')
