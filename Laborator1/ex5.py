"""
5. Write a function that checks whether a string contains special characters (\r, \t, \n, \a, \b, \f, \v)
"""


def contains_special_characters(text):
    special_characters = ['\r', '\t', '\n', '\a', '\b', '\f', '\v']
    for character in special_characters:
        if character in text:
            return True
    return False


print(contains_special_characters('am\trezolvat\nexercitiile'))