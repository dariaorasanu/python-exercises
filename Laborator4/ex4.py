"""
4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem, parcurge recursiv structura
de fisiere si directoare pe care acesta le contine si afiseaza in consola toate path-urile pe care le-a parcurs
(output similar cu outputul de pe slide-ul cu os.walk din curs DAR sa includa si directoarele intalnite in fiecare director
nu doar fisierele, folderele sa fie urmate de un '\\' la printare, e.g. .\\folder1\\). NU aveti voie sa folositi os.walk.
"""
import os


def parse_dir(path):
    try:
        if os.path.isdir(path):
            print(f"{path}\\")
            for entry in os.listdir(path):
                full_path = os.path.join(path, entry)
                parse_dir(full_path)
        elif os.path.isfile(path):
            print(path)
        else:
            print('Calea nu este valida.')
    except OSError as e:
        print(f"Eroare la accesarea '{path}': {e}")


print(parse_dir(r"D:\FACULTATE\ASII"))