"""
7. Fie un dictionar global definit asemanator cu cel de mai sus, cu deosebirea ca functiile date ca valori ale dictionarului poate primi
orice combinatie de parametri. Sa se scrie o functie apply_function care primeste ca parametru numele unei operatii si aplica functia
corespunzatoare peste argumentele primite. Sa se implementeze astfel incat, in cazul adaugarii unei functii noi, sa nu fie necesara modificarea functiei apply_function.
Un exemplu de dictionar global ar putea fi urmatorul:
{
   "print_all": lambda *a, **k: print(a, k),
   "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
   "print_only_args": lambda *a, **k: print(a),
   "print_only_kwargs": lambda *a, **k: print(k)
}
"""

global_dictionary = {
   "print_all": lambda *a, **k: print(a, k),
   "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
   "print_only_args": lambda *a, **k: print(a),
   "print_only_kwargs": lambda *a, **k: print(k)
}


def apply_function(operator, *a, **k):
    global_dictionary[operator](*a, **k)

print(apply_function('print_all', (1, 2, 3), cheie1=54, cheie2=3, cheie3=27))
print(apply_function('print_only_kwargs', (1, 2, 3), cheie1=54, cheie2=3, cheie3=27))

