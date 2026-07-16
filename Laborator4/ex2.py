"""
2. Scrieti un script care primeste ca parametru de la linia de comanda un path si afiseaza primii 4096 bytes daca path-ul
duce la un fisier, intrarile din acesta daca path-ul reprezinta un director si un mesaj de eroare daca path-ul nu este unul valid.
"""
import sys
import os
try:
    path = sys.argv[1]
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            data = f.read(4096)
            print(data)
    elif os.path.isdir(path):
        for entry in os.listdir(path):
            print(entry)
    else:
        print("Path-ul nu este valid")
except IndexError:
    print("Trebuie introdusa o cale la linia de comanda")
except Exception as e:
    print(f"A aparut o eroare:{str(e)}")
