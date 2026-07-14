"""
5. Fie functia validate_dict care primeste ca parametru un set de tuple care reprezinta reguli de validare pentru un dictionar
si un dictionar cu chei de tipul string si valori tot de tipul string. O regula este definita astfel: (cheie, "prefix", "middle", "sufix").
O valoare este considerata valida daca incepe cu "prefix", "middle" se gaseste in interiorul valorii (nu la inceput sau sfarsit)
si se sfarsete cu "sufix". Functia va returna True daca dictionarul dat ca parametru respecta toate regulile si daca nu apar in dictionar
decat chei care sunt mentionate si in reguli, False in caz contrar.
Exemplu: regulile [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")] si dictionarul
{"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside", "key3": "this is not valid"}
=> False deoarece desi regulile sunt respectate pentru "key1" si "key2", apare "key3" care nu apare in reguli.
"""


def validate_dict(rules, dictionary):
    allowed_keys = {rule[0] for rule in rules}

    if set(dictionary.keys()) - allowed_keys:
        return False

    for rule in rules:
        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        sufix = rule[3]
        value = dictionary[key]
        #prefix
        if not value.startswith(prefix):
            return False
        #sufix
        if not value.endswith(sufix):
            return False
        #middle
        if prefix:
            start_idx = len(prefix)
        else:
            start_idx = 1
        if sufix:
            end_idx = -len(sufix)
        else:
            end_idx = -1
        middle_zone = value[start_idx:end_idx]
        if middle not in middle_zone:
            return False
    return True

print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")], {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside"}))