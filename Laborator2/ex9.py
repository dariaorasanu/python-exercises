"""
9.	Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui de-al 2-lea element din tuplă.
Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
"""


def sort_string_tuples(string_list):
    sorted_list = sorted(string_list, key = lambda i: i[1][2])
    return sorted_list

print(sort_string_tuples([('avc', 'bcd'), ('abc', 'zza')]))

