"""
1.	Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.
"""


def fibonnacci_first_n(n):
    if n == 1:
        return [0]
    fib_list = [0, 1]
    i = 2
    while i < n:
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
        i = i + 1
    return fib_list

print(fibonnacci_first_n(9))

