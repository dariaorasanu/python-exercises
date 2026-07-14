"""
3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii, si/sau semne de punctuatie (, ;, ? ! . )
Intre 2 cuvinte pot aparea in orice combinatie spatii si semne de punctuatie
"""


def is_letter(letter):
    letter = letter.lower()
    if 'a' <= letter <= 'z':
        return True
    return False


def is_separator(letter):
    if letter in ' ,.;?!':
        return True
    return False


def words_count(text):
    words = 0
    for i in range(len(text)):
        if i == 0 and is_letter(text[i]):
            words = words + 1
        if is_letter(text[i]) and is_separator(text[i - 1]):
            words = words + 1
    return words


print(words_count(' ; aici,am!   patru  .  ;  cuvinte?'))
#fara cuvinte:
print(words_count('  ;? '))


def words_count_with_zip(text):
    words = 0
    if is_letter(text[0]):
        words = words + 1
    for precedent, current in zip(text[:-1], text[1:]):
        if is_separator(precedent) and is_letter(current):
            words += 1
    return words

print(words_count_with_zip(' ; aici,am!   patru  .  ;  cuvinte?'))