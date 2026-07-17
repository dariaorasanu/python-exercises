"""
8. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem:
■	versiunea de python folosita. Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ===" iar daca se
foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
■	numele user-ului care a executat scriptul,
■	path-ul complet al scriptului.
■	path-ul directorului in care se afla scriptul,
■	tipul sistemului de operare,
■	numarul de core-uri,
■	directoarele din PATH-ul procesului cate unul pe linie
"""
import os
import platform
import sys


def display_system_info():
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Python Version: {python_version}")

    if sys.version_info.major == 2:
        print("=== Python 2 ===")
    elif sys.version_info.major == 3:
        print("Running under Py3")

    username = os.getlogin()
    print(f"User: {username}")

    script_path = os.path.abspath(sys.argv[0])
    print(f"Script Full Path: {script_path}")

    script_dir = os.path.dirname(script_path)
    print(f"Script Directory: {script_dir}")

    os_type = platform.system()
    print(f"OS Type: {os_type}")

    cpu_cores = os.cpu_count()
    print(f"CPU Cores: {cpu_cores}")

    print("Directories in PATH:")
    path_directories = os.environ.get("PATH", "").split(os.pathsep)
    for directory in path_directories:
        if directory:
            print(directory)

try:
    display_system_info()
except Exception as e:
    print(f"An error occurred while fetching system data: {str(e)}")