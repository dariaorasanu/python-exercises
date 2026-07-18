"""
11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de caractere care reprezinta calea catre un
fisier si returneaza un dictionar cu urmatoarele campuri:
full_path = calea absoluta catre fisier,
file_size = dimensiunea fisierului in octeti,
file_extension = extensia fisierului (daca are) sau "",
can_read si can_write = True/False daca se poate citi din/scrie in fisier.
"""
import os


def get_file_info(path):
    dictionary = {}
    #full path
    full_path = os.path.abspath(path)
    dictionary["full_path"] = full_path
    #file_size
    file_size = os.path.getsize(path)
    dictionary["file_size"] = file_size
    #file_extension
    file_extension = os.path.splitext(path)[1]
    if file_extension:
        #scot punctul din extensie
        file_extension = file_extension[1:]
    dictionary["file_extension"] = file_extension
    #read
    can_read = os.access(path, os.R_OK)
    dictionary["can_read"] = can_read
    #write
    can_write = os.access(path, os.W_OK)
    dictionary["can_write"] = can_write
    return dictionary

try:
    for key, value in get_file_info('ex11.py').items():
        print(f"{key}: {value}")
except OSError as e:
    print(f"Eroare la accesarea fisierului: {str(e)}")
except Exception as e:
    print(f"A apărut o eroare: {str(e)}")
