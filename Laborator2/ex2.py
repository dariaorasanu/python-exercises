"""
2.	Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.
"""


def is_prime(number):
    if number == 0 or number == 1:
        return False
    if number % 2 == 0 and number != 2:
        return False
    for i in range (3, int (number ** (1 / 2)) + 1, 2):
        if number % i == 0:
            return False
    return True

#var1
def prime_numbers(int_list):
    result =[]
    for number in int_list:
        if is_prime(number):
            result.append(number)
    return result


#var2: list comprehension
def prime_numbers_with_list_comprehension(int_list):
    result = [number for number in int_list if is_prime(number)]
    return result


print(prime_numbers([2, 3, 6, 5, 8, 11, 27, 29]))
print(prime_numbers_with_list_comprehension([2, 3, 6, 5, 8, 11, 27, 29]))