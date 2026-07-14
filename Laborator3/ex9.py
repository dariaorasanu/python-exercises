"""
9. Sa se scrie o functie care primeste un numar variabil de seturi si returneaza un dictionar cu urmatoarele operatii
dintre toate seturile doua cate doua: reuniune, intersectie, a-b, b-a. Cheia va avea urmatoarea forma: "a op b",
unde a si b sunt doua seturi, iar op este operatorul aplicat: |, &, -. Valoarea va fi numarul de elemente din rezultatul operatiei.
Ex: {1,2}, {2, 3} =>
{
   "{1, 2} | {2, 3}": 3,
   "{1, 2} & {2, 3}": 1,
   "{1, 2} - {2, 3}": 1,
   ...
}
"""


def operations_on_sets(*sets):
    my_dict = dict()
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            my_dict[f'{set1} | {set2}'] = len(set1 | set2)
            my_dict[f'{set1} & {set2}'] = len(set1 & set2)
            my_dict[f'{set1} - {set2}'] = len(set1 - set2)
            my_dict[f'{set2} - {set1}'] = len(set2 - set1)
    return my_dict

print(operations_on_sets({1,2}, {2, 3}))


