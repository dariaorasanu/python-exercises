"""
10. Sa se scrie o functie search_by_content care primeste ca parametru doua siruri de caractere target si to_search si returneaza
o lista de fisiere care contin to_search. Fisierele se vor cauta astfel: daca target este un fisier, se cauta doar in fisierul
respectiv iar daca este un director se va cauta recursiv in toate fisierele din acel director. Daca target nu este nici fisier
nici director, se va arunca o exceptie de tipul ValueError cu un mesaj corespunzator.
"""
import os


def search_by_content(target, to_search):
    result = []
    if os.path.isfile(target):
        with open(target, 'rt') as f:
            for line in f:
                if to_search in line:
                    result.append(target)
                    break
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for f in files:
                full_file_path = os.path.join(root, f)
                with open(full_file_path, 'rt', encoding="utf-8", errors='ignore') as file:
                    for line in file:
                        if to_search in line:
                            result.append(full_file_path)
                            break
    else:
         raise ValueError("Primul parametru nu este nici fisier nici director")
    return result

try:
    found_files = search_by_content(r"C:\Users\Daria\Desktop\Internship", "daria")
    for file_path in found_files:
        print(file_path)
except OSError as e:
    print(f"Eroare la accesarea fisierelor: {str(e)}")
except Exception as e:
    print(f"A apărut o eroare: {str(e)}")
