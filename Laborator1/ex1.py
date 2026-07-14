"""
1.  Find the largest common divisor of multiple numbers.
Define a function with variable number of parameters to resolve this.
"""


def largest_common_divisor_of2(number1, number2):
    while number2 != 0:
        rest = number1 % number2
        number1 = number2
        number2 = rest
    return number1


def largest_common_divisor(*numbers):
    largest_divisor = largest_common_divisor_of2(numbers[0], numbers[1])
    for number in numbers:
        largest_divisor = largest_common_divisor_of2(largest_divisor,number)

    return largest_divisor

print(largest_common_divisor(24, 16, 44, 4, 8))








