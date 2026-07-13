"""
4.	Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza: a intersectat cu b, a reunit cu b, a - b, b – a fara a folosi set-uri.
"""


def operations_on_sets(a, b):
    # a intersectat cu b
    intersection = []
    i = 0
    while i < len(a):
        if a[i] not in intersection and a[i] in b:
            intersection.append(a[i])
        i = i + 1

    #a reunit cu b
    reunion = []
    i = 0
    while i < len(a):
        if a[i] not in reunion:
            reunion.append(a[i])
        i = i + 1
    j = 0
    while j < len(b):
        if b[j] not in reunion:
            reunion.append(b[j])
        j = j + 1

    # a - b
    a_minus_b =[]
    i = 0
    while i < len(a):
        if a[i] not in a_minus_b and a[i] not in b:
            a_minus_b.append(a[i])
        i = i + 1

    # b - a
    b_minus_a = []
    j = 0
    while j < len(b):
        if b[j] not in b_minus_a and b[j] not in a:
            b_minus_a.append(b[j])
        j = j + 1

    return intersection, reunion, a_minus_b, b_minus_a

print(operations_on_sets([0,1,2,3,4,5], [3,4,5,6,7,8]))
