"""
1.Create a module that contains a function named "sort_uuids". This function reads the file sample.txt ( download ), and
sorts the lines based on the string that is between the first and second dash ("-").
Ex: 00e43761-e18a-40c6-b252-3407aa1d8e45 => is sorted by "e18a".  There might be situations where the code might raise Exception.
Catch them all ! Create a new file, named "results.txt". Write in this file the sorted uuids.
"""


def sort_uuids():
    try:
        uuids = {}
        with open("sample.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    uuid_second_part = line.split('-')[1]
                    uuids[line] = uuid_second_part
        sorted_uuids = sorted(uuids.items(), key=lambda item: item[1])
        with open("result.txt", 'w') as f:
            for key, value in sorted_uuids:
                f.write(f'{key}\n')
    except OSError as e:
        print(f"Eroare la citirea/scrierea in fisier: {str(e)}")
    except Exception as e:
        print(f"A aparut o alta eroare: {str(e)}")



