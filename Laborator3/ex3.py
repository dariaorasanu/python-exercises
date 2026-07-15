"""
3. Sa se compare doua dictionare fara a folosi operatorul "==" sau "!=" pentru altceva decat tipuri primitive (int, float, str)
si sa se returneze un tuplu de liste de diferente astfel: (cheile_comune_dar_cu_valori_diferite, cheile_care_se_gasesc_doar_in_primul_dict, cheile_care_se_gasesc_doar_in_al_doilea_dict).
(Atentie, dictionarele trebuiesc parcurse recursiv deoarece la randul lor pot contine alte containere, cum ar fi dictionare, liste, set-uri, etc.)
"""


def compare_sets_v1(set1, set2):
    if len(set1) != len(set2):
        return False

    for item1 in set1:
        ok = False
        for item2 in set2:
            if are_equal(item1, item2):
                ok = True
                break
        if not ok:
            return False
    return True


def compare_sets_v2(set1, set2):
    diff1 = set1 - set2
    diff2 = set2 - set1
    if not diff1.isdisjoint(diff1) or not diff2.isdisjoint(diff2):
        return False
    return True


def are_equal(element1, element2):
    if type(element1) != type(element2):
        return False

    elif type(element1) == type(element2) and type(element1) in (int, float, str, bool):
        return element1 == element2

    elif type(element1) is list:
        if len(element1) != len(element2):
            return False
        pairs = zip(element1, element2)
        for pair in pairs:
            if not are_equal(pair[0],pair[1]):
                return False

    elif type(element1) is dict:
        if len(element1) != len(element2):
            return False
        for key in element1:
            if key not in element2:
                return False
            if not are_equal(element1[key], element2[key]):
                return False

    elif type(element1) is set:
        return compare_sets_v1(element1, element2)

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

