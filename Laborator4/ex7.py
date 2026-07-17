"""
7. Sa se scrie un script care primeste urmatoarele argumente: path, depth, filesize , filecount, dircount si care creeaza
o structura de directoare de adancime depth astfel: incepand din radacina path vor fi create dircount directoare si filecount
fisiere cu continut de filesize octeti (doar caracterul "a" de exemplu") iar acest proces va fi repetat recursiv pentru
fiecare director creat pana cand se obtine adancimea dorita (in directoarele aflate la adacimea maxima nu se vor crea alte directoare)
De exemplu, daca rulam scriptul astfel: python3 create_dummy_tree.py test 2 1024 3 3 va fi creat in directorul curent urmatoarea structura:
   test
   test/dir0
   test/dir0/file1 (size 1024)
   test/dir0/file2 (size 1024)
   test/dir0/file3 (size 1024)
   test/dir1
   test/dir1/file1 (size 1024)
   test/dir1/file2 (size 1024)
   test/dir1/file3 (size 1024)
   test/dir2
   test/dir2/file1 (size 1024)
   test/dir2/file2 (size 1024)
   test/dir2/file3 (size 1024)
   test/file0 (size 1024)
   test/file1 (size 1024)
   test/file2 (size 1024)

"""
import os
import sys


def create_tree(path, level, depth, file_size, file_count, dir_count):
    os.mkdir(path)

    for i in range(file_count):
        file_name = os.path.join(path, f"file{i}")

        with open(file_name, "w") as f:
            f.write("a" * file_size)

    if level < depth - 1:
        for i in range(dir_count):
            dir_name = os.path.join(path, f"dir{i}")
            create_tree(dir_name, level + 1, depth, file_size, file_count, dir_count)


try:
    path = sys.argv[1]
    depth = int(sys.argv[2])
    file_size = int(sys.argv[3])
    file_count = int(sys.argv[4])
    dir_count = int(sys.argv[5])

    create_tree(path, 0, depth, file_size, file_count, dir_count)

except IndexError:
    print("Trebuie introdusi 5 parametri.")
except ValueError:
    print("Depth, filesize, filecount si dircount trebuie sa fie numere intregi.")
except OSError as e:
    print(f"Eroare la crearea structurii: {str(e)}")
except Exception as e:
    print(f"A apărut o eroare: {str(e)}")
