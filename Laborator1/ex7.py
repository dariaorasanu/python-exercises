"""
7. Write a function that receives a char_len integer and a variable number of strings
and checks that each two neighboring strings follow the following rule:
the second string starts with the last char_len characters of the first string (like the word game pheasant).
"""

#var1:


def check_word_game(char_len, *strings):
    for i in range (1, len(strings)):
        string1 = strings[i - 1]
        string2 = strings[i]
        if not string1[-char_len:] == string2[:char_len]:
            return False

    return True

#True:
print(check_word_game(2, 'daria', 'iasomie', 'ierbivor', 'orb'))
print(check_word_game(3, 'rest', 'estetic', 'tichinea', 'nea'))
#False:
print(check_word_game(3, 'rest', 'estetic', 'tactica'))

#var2 (cu zip):

def check_word_game2(char_len, *strings):
    grouped_words = zip(strings[:-1], strings[1:])

    for word1, word2 in grouped_words:
        if word1[-char_len:] != word2[:char_len]:
            return False
    return True


#True:
print(check_word_game2(2, 'daria', 'iasomie', 'ierbivor', 'orb'))
print(check_word_game2(3, 'rest', 'estetic', 'tichinea', 'nea'))
#False:
print(check_word_game2(3, 'rest', 'estetic', 'tactica'))



