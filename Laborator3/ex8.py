"""
8. Sa se scrie o functie care primeste ca parametru un set si returneaza un tuplu (a, b), a reprezentand numarul de
elemente unice din set iar b reprezentand numarul de elemente duplicate din set.
"""
# aici presupun ca enuntul trebuia sa fie ca se da o lista si sa returnez elementele duplicate si cele unice, pentru ca
# daca primesc set nu am cum sa am duplicate


def extract_unique_and_duplicates_from_list(l):
    frequency = {}
    for element in l:
        if element not in frequency:
            frequency[element] = 1
        else:
            frequency[element] += 1
    uniques = 0
    duplicates = 0
    for value in frequency.values():
        if value == 1:
            uniques += 1
        else:
            duplicates += 1
    return (uniques, duplicates)

print (extract_unique_and_duplicates_from_list([1, 2, 2, 3, 3, 3, 4]))

