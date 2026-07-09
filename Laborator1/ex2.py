'''
2. Write a function that calculates how many vowels are in a string.
'''

def is_vowel (letter):
    letter = letter.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    return False
def vowels_count (string):
    vowels = 0
    for i in range(0, len(string)):
        if is_vowel(string[i]):
            vowels = vowels + 1
    return vowels

print (vowels_count('DAria'))
