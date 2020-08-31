from datetime import datetime


#  O(N) => takes N steps to conclude the function, is based on the input
def sum_1(n: int):
    sum_of_n_values = 0
    for i in range(n + 1):
        sum_of_n_values += i
    return sum_of_n_values


#  O(3) => only takes 3 steps to return the result, independently of n
def sum_2(n: int):
    return n * (n + 1) / 2


def run(function, n):
    start_time = datetime.now()
    function(n)
    duration = datetime.now() - start_time
    return duration.microseconds


print(run(sum_1, 10))
print(run(sum_2, 10))
