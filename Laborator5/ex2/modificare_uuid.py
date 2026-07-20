"""
2. Using the same file from Problem 1 (sample.txt), modify the line(s) that does not respect the uuid format (if there is any).
This modification means to replace the bad line with this message "|INVALID_UUID|". A good way to „modify” a file
is to create an entirely new file with the desired content, delete the file that you want to change, and rename the
new file to be named the same as the old file.
"""
import os
import uuid


def is_valid_uuid(uuid_str):
    uuid_str = uuid_str.strip()
    if len(uuid_str) != 36:
        return False
    try:
        uuid.UUID(uuid_str)
        return True
    except ValueError:
        print("Stringul dat nu este un uuid valid")
        return False


def modify_uuids(file_path="sample.txt"):
    temp_file_path = "sample_temp.txt"
    try:
        with open(file_path, 'r') as f_r:
            with open(temp_file_path, 'w') as f_w:
                for line in f_r:
                    line = line.strip()
                    if is_valid_uuid(line) and line:
                        f_w.write(f'{line}\n')
                    else:
                        f_w.write("|INVALID_UUID|\n")
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
    except OSError as e:
        print(f"Eroare la citirea/scrierea in fisier: {str(e)}")
    except Exception as e:
        print(f"A aparut o alta eroare: {str(e)}")
