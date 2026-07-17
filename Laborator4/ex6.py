"""
6. Scrieti un script care primeste 3 parametri de la consola. Primul va fi un path catre un fisier, al doilea un path
catre un director iar al treilea va fi dimensiunea unui buffer. Scriptul va copia fisierul dat ca parametru in
directorul dat ca parametru, utilizand un buffer de marimea celui de-al treilea parametru, in bytes.
"""
import sys
import os
try:
    source_file = sys.argv[1]
    destination_directory = sys.argv[2]
    buffer_size = int(sys.argv[3])


    file_name = os.path.basename(source_file)
    destination_file = os.path.join(destination_directory, file_name)
    with open(source_file, "rb") as src, open(destination_file, "wb") as dest:
        while True:
            block = src.read(buffer_size)

            if not block:
                break

            dest.write(block)
except IndexError:
    print("Trebuie sa introduci exact doi parametri")
except OSError as e:
    print(f'Eroare la copierea intre fisiere: {str(e)}')
except Exception as e:
    print(f'A aparut o eroare: {str(e)}')
