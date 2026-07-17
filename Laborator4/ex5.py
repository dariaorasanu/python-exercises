"""
5. Scrieti un script care primeste 2 parametri de la linia de comanda reprezentand un path catre un director de pe
sistem si un nume de fisier. Scriptul va parcurge recursiv structura de fisiere si directoare din directorul dat ca
parametru, utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si tipul
acestuia (FILE, DIRECTORY, separate de |. Fiecare path va fi scris pe cate o linie.

"""
import os
import sys

try:
    source_directory = sys.argv[1]
    output_filename = sys.argv[2]
    with open(output_filename, "w") as out_file:
        for root, dirs, files in os.walk(source_directory):
            for directory in dirs:
                full_dir_path = os.path.join(root, directory)
                out_file.write(f"{full_dir_path}\\|DIRECTORY\n")

            for file in files:
                full_file_path = os.path.join(root, file)
                out_file.write(f"{full_file_path}|FILE\n")

except IndexError:
    print("Trebuie sa introduci exact doi parametri")
except OSError as e:
    print(f'Eroare la accesarea fisierelor sau directoarelor: {str(e)}')
except Exception as e:
    print(f'A aparut o eroare: {str(e)}')