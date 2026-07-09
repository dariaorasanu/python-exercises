'''
4. Write a function that receives two strings as parameters and
returns the number of occurrences of the first string in the second.
'''
def occurrences_count (small_string, main_string):
    occurrences = 0
    for i in range (0, len(main_string)):
        if main_string[i : i + len(small_string)] == small_string:
            occurrences = occurrences + 1

    return occurrences
print(occurrences_count('ana', 'ioana'))

print(occurrences_count('aa', 'aaaa'))