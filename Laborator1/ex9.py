'''
9. Write a function that returns the largest prime number from a string given as a parameter or -1
if the character string contains no prime number.
 Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271
'''

def is_prime (number):
    if number == 0 or number == 1:
        return False
    if number % 2 == 0:
        return False
    for i in range (3, int (number ** (1 / 2)), 2):
        if number % i == 0:
            return False
    return True

def largest_prime_number (text):
    prime_number = -1
    for i in range(0, len(text)):
        if '0' <= text[i] <= '9':
            number = int(text[i])
            i = i + 1
            while '0' <= text[i] <= '9':
                number = number * 10 + int(text[i])
                i = i + 1
            i = i -1
            if is_prime(number) and number > prime_number:
                prime_number = number
    return prime_number

print (largest_prime_number('ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'))

