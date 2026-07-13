"""
2. Write a function that calculates how many vowels are in a string.
"""

def is_vowel(letter):
    letter = letter.lower()
    if letter in 'aeiou':
        return True
    return False


def vowels_count(text):
    vowels = 0
    for letter in text:
        if is_vowel(letter):
            vowels = vowels + 1
    return vowels

print(vowels_count('DAria'))
