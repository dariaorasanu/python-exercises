"""
2. Scrieti o functie care primeste ca parametru un sir de caractere si returneaza un dictionar in care cheile sunt caracterele din componenta sirului de caractere iar valorile sunt reprezentate de numarul de aparitii ale caracterului respectiv in textul dat.
Exemplu: Pentru sirul "Ana are mere." dat ca parametru functia va returna dictionarul: {'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}. Daca gasiti modul usor va rog sa o faceti si la mana 😊.
"""


def characters_frequency_in_string(text):
    result = dict()
    for character in text:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

print (characters_frequency_in_string("Ana are mere"))