"""
1. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza un tuplu de seturi care sa contina: (a intersectat cu b, a reunit cu b, a - b, b - a)
"""


def operations_on_sets(a, b):
    a = set(a)
    b = set(b)
    result = (a & b, a | b, a - b, b - a)
    return result

print(operations_on_sets([0, 1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8]))
