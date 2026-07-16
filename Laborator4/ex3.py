"""
3. Scrieti o functie care primeste ca parametru un nume de fisier. Aceasta va scrie in fisier datele din os.environ,
fiecare linie continand cate o intrare din acest dictionar, sub forma cheie [tab] (\t) valoare.
"""
import os


def display_data_about_file(file_name):
    try:
        with open(file_name, 'w') as f:
            for key, value in os.environ.items():
                f.write(f'{key}\t{value}\n')
    except OSError as e:
        print(f'Eroare la scrierea în fișier: {str(e)}')
    except Exception as e:
        print(f'A apărut o eroare neașteptată: {str(e)}')


display_data_about_file("mediu.txt")