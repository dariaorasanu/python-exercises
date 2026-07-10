'''
2.	Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.
'''

def is_prime (number):
    if number == 0 or number == 1:
        return False
    if number % 2 == 0:
        return False
    for i in range (3, int (number ** (1 / 2)), 2):
        if number % i == 0:
            return False
    return True

def prime_numbers (int_list):
    result =[]
    for number in int_list:
        if is_prime(number):
            result.append(number)
    return result

print(prime_numbers([3, 6, 5, 8, 11, 27, 29]))