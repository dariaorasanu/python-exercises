"""
13. Sa se scrie o funcție ce returnează o lista cu toate fisierele dintr-un director(primit ca parametru), ce au o anumita
extensie (primita ca parametru).
Sa se scrie o functie clasifica ce va copia fisierele returnate de la funcția anterioară în felul următor:
- în 5 directoare cu nume specific, in functie de size - (0-10KB, 10KB-1MB, 1MB-2MB, 2MB-5MB, 5MB-)
- în 26 directoare cu nume specific, in functie de primul caracter din nume (A, B, C, ...)
- în 2 directoare cu nume specific - numele format doar din litere sau nu
HINT: se vor crea intai (prin cod) directoarele cu numele sugerate.
"""
import os
import shutil


def files_from_directory(directory, extension):
    result = []
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path) and item.endswith(extension):
            result.append(full_path)
    return result


def clasify_files(directory, files_list):
    base_folder = os.path.join(directory, "Rezultate")
    #directoare pentru dimensiuni:
    folder_size_1 = os.path.join(base_folder, "size_0_10KB")
    folder_size_2 = os.path.join(base_folder, "size_10KB_1MB")
    folder_size_3 = os.path.join(base_folder, "size_1MB_2MB")
    folder_size_4 = os.path.join(base_folder, "size_2MB_5MB")
    folder_size_5 = os.path.join(base_folder, "size_5MB_plus")

    os.makedirs(folder_size_1, exist_ok=True)
    os.makedirs(folder_size_2, exist_ok=True)
    os.makedirs(folder_size_3, exist_ok=True)
    os.makedirs(folder_size_4, exist_ok=True)
    os.makedirs(folder_size_5, exist_ok=True)

    #directoare pentru primul caracter A-Z:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        folder_letter = os.path.join(base_folder, letter)
        os.makedirs(folder_letter, exist_ok=True)

    #directoare doar pt litere si doar pt cifre:
    folder_only_letters = os.path.join(base_folder, "Nume_doar_litere")
    folder_other_than_letters = os.path.join(base_folder, "Nume_doar_cifre")

    os.makedirs(folder_only_letters, exist_ok=True)
    os.makedirs(folder_other_than_letters, exist_ok=True)

    #clasificarea:
    for f in files_list:
        file_name = os.path.basename(f)
        #dimensiune:
        size = os.path.getsize(f)
        if size <= 10 * 1024:
            shutil.copy(f, folder_size_1)
        elif size <= 1 * 1024 * 1024:
            shutil.copy(f, folder_size_2)
        elif size <= 2 * 1024 * 1024:
            shutil.copy(f, folder_size_3)
        elif size <= 5 * 1024 * 1024:
            shutil.copy(f, folder_size_4)
        else:
            shutil.copy(f, folder_size_5)

        #litera cu care incepe:
        first_letter = file_name[0].upper()
        if first_letter.isalpha():
            destination_folder = os.path.join(base_folder, first_letter)
            shutil.copy(f, destination_folder)

        #doar litere sau doar cifre:
        name_without_extension = os.path.splitext(file_name)[0]

        if name_without_extension.isalpha():
            shutil.copy(f, folder_only_letters)
        else:
            shutil.copy(f, folder_other_than_letters)

try:
    path_directory = r"C:\Users\Daria\Desktop\test"
    ext = ".txt"

    found_files = files_from_directory(path_directory, ext)

    if found_files:
        clasify_files(path_directory, found_files)
        print(f"Am clasificat cu succes {len(found_files)} fisiere in folderul 'Rezultate'!")
    else:
        print(f"Nu s-a gasit niciun fisier cu extensia '{ext}' in directorul specificat.")
except OSError as e:
    print(f"Eroare la accesarea fisierelor sau directoarelor: {str(e)}")
except Exception as e:
    print(f"A apărut o eroare: {str(e)}")
