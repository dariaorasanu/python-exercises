"""
12. Sa se scrie o functie get_dirs_info care primeste ca parametru un sir de caractere care reprezinta calea catre un
director si returneaza un dictionar cu urmatoarele informatii:
full_path = calea absoluta catre director,
total_size = dimensiunea totala (cumulata) a tuturor fisierelor din acel director,
files = calea relativa catre toate fisierele din acel director, grupate dupa adancime.
dirs = calea absoluta catre toate directoarele din acel director cu toate informatiile corespunzatoare.
Sa se scrie intr-un fisier output.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa numarul de fisiere cu adancimea 2.
Sa se scrie intr-un fisier size.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa total_size.
Sa se scrie intr-un fisier lungime.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa numarul maxim de caractere din numele fișierelor.
"""
import os


def get_dirs_info(target):
    target = os.path.abspath(target)

    result = {
        "full_path": target,
        "total_size": 0,
        "files": {},
        "dirs": []
    }
    for root, dirs, files in os.walk(target):
        for f in files:
            full_file_path = os.path.join(root, f)
            result["total_size"] += os.path.getsize(full_file_path)
            if 1 not in result["files"]:
                result["files"][1] = []
            result["files"][1].append(f)

        for d in dirs:
            full_dir_path = os.path.join(root, d)
            subdir_info = get_dirs_info(full_dir_path)

            result["dirs"].append(subdir_info)
            result["total_size"] += subdir_info["total_size"]

            for depth in subdir_info["files"]:
                files_list = subdir_info["files"][depth]

                if (depth + 1) not in result["files"]:
                    result["files"][depth + 1] = []
                result["files"][depth + 1].extend(files_list)

        break

    return result


# numara cate fisiere sunt la o anumita adancime intr-un director
def get_files_at_depth(info_dir, depth):
    if depth in info_dir["files"]:
        return len(info_dir["files"][depth])
    else:
        return 0


# gaseste lungimea celui mai lung nume de fisier dintr-un director
def len_max_file_name(info_dir):
    max_len = 0

    for depth in info_dir["files"]:
        for file_name in info_dir["files"][depth]:
            if len(file_name) > max_len:
                max_len = len(file_name)

    return max_len


# scrie intr-un fisier numele directoarelor, sortate descrescator
def write_sorted_dir(output_file_name, dir_list, sort_key):
    sorted_dir = sorted(dir_list, key=sort_key, reverse=True)

    with open(output_file_name, "w", encoding="utf-8") as f:
        for directory in sorted_dir:
            dir_name = os.path.basename(directory["full_path"])
            f.write(dir_name + "\n")



def depth2_files(director):
    return get_files_at_depth(director, 2)


def size_criteria(director):
    return director["total_size"]


def length_name_criteria(director):
    return len_max_file_name(director)


try:
    res = get_dirs_info(r"C:\Users\Daria\Desktop\test")
    directories = res["dirs"]

    write_sorted_dir("output.txt", directories, depth2_files)
    write_sorted_dir("size.txt", directories, size_criteria)
    write_sorted_dir("lungime.txt", directories, length_name_criteria)

except OSError as e:
    print(f"Eroare la accesarea fisierelor sau directoarelor: {str(e)}")
except Exception as e:
    print(f"A apărut o eroare: {str(e)}")

