'''
3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii, si/sau semne de punctuatie (, ;, ? ! . )
Intre 2 cuvinte pot aparea in orice combinatie spatii si smne de punctuatie
'''
def is_letter(letter):
    letter = letter.lower()
    if 'a' <= letter <= 'z':
        return True
    return False

def is_separator(letter):
    if letter == ' ' or letter == ',' or letter == ';' or letter == '?' or letter == '!' or letter == '.':
        return True
    return False

def words_count (string):
    words = 0
    for i in range(0, len(string)):
        if i == 0 and is_letter(string[i]):
            words = words + 1
        if is_letter(string[i]) == True and  is_separator(string[i - 1]) == True:
            words = words + 1
    return words

print (words_count(' ; aici,am!   patru  .  ;  cuvinte?'))
#fara cuvinte:
print (words_count('  ;? '))