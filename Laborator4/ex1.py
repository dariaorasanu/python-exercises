"""
1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
a) a-b
b) a+b
c) a/b
d) a*b
"""
import sys


def operations_on_two_numbers(a, b):
    print(a - b, a + b, a / b, a * b)

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    operations_on_two_numbers(a, b)
except IndexError:
    print("Nu ai introdus ambele numere in linia de comanda")
except ValueError:
    print("Trebuie introduse doua numere.")
except ZeroDivisionError:
    print("Impartirea la zero nu este permisa.")
except Exception as e:
    print(f"A aparut eroarea: {str(e)}")
