"""
4*. Rezolvati ex. 4 dar folositi os.walk.
"""

import os


def parse_dir_with_walk(path):
    try:
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                full_dir_path = os.path.join(root, directory)
                print(f"{full_dir_path}\\")

            for file in files:
                full_file_path = os.path.join(root, file)
                print(full_file_path)

    except OSError as e:
        print(f"Eroare la accesarea '{path}': {e}")


parse_dir_with_walk(r"D:\FACULTATE\ASII")