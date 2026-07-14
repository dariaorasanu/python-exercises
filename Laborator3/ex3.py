"""
3. Sa se compare doua dictionare fara a folosi operatorul "==" sau "!=" pentru altceva decat tipuri primitive (int, float, str)
si sa se returneze un tuplu de liste de diferente astfel: (cheile_comune_dar_cu_valori_diferite, cheile_care_se_gasesc_doar_in_primul_dict, cheile_care_se_gasesc_doar_in_al_doilea_dict).
(Atentie, dictionarele trebuiesc parcurse recursiv deoarece la randul lor pot contine alte containere, cum ar fi dictionare, liste, set-uri, etc.)
"""


def are_equal(element1, element2):
    if type(element1) != type(element2):
        return False

    elif type(element1) == type(element2) and type(element1) in (int, float, str, bool):
        return element1 == element2

    elif type(element1) == list:
        if len(element1) != len(element2):
            return False
        for i in range(len(element1)):
            if not are_equal(element1[i], element2[i]):
                return False

    elif type(element1) == dict:
        if set(element1.keys()) != set(element2.keys()):
            return False
        for key in element1:
            if not are_equal(element1[key], element2[key]):
                return False

    elif type(element1) == set and type(element2) == set:
        if element1 - element2 != set() and element2 - element1 != set():
            return False

    return True


def compare_dictionaries(dict1, dict2):
    dict1_set = set(dict1)
    dict2_set = set(dict2)
    common_keys_with_different_values = []
    for key in dict1_set & dict2_set:
        val1 = dict1[key]
        val2 = dict2[key]
        if not are_equal(val1, val2):
            common_keys_with_different_values.append(key)
    result = (common_keys_with_different_values, list(dict1_set - dict2_set), list(dict2_set - dict1_set))
    return result

print(compare_dictionaries({'a' : 2, 'b' : 5, 'c' : 1}, {'a' : 2, 'd' : 5, 'c' : 2}))

#liste
d1 = {"student": "Daria", "note": [10, 8, 9]}
d2 = {"student": "Daria", "note": [10, 8, 10]}

print(compare_dictionaries(d1, d2))

#dictionare
dict_a = {
    "user1": {"nume": "Ana", "varsta": 22},
    "user2": {"nume": "Alex", "varsta": 25},
    "doar_in_a": 100
}
dict_b = {
    "user1": {"nume": "Ana", "varsta": 22},
    "user2": {"nume": "Alex", "varsta": 26},
    "doar_in_b": 200
}
print(compare_dictionaries(dict_a, dict_b))


#seturi
d3 = {"culori": {"rosu", "albastru"}}
d4 = {"culori": {"albastru", "rosu"}}

print(compare_dictionaries(d3, d4))
