'''
6.	Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [7, 1, "test"] si x = 2 se va returna [1, 2, 3, 4]
# 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2, 4 se afla in listele 2 si 3.
'''

def frequency_x (x, *lists):
    union = []
    for l in lists:
        for element in l:
            union.append(element)
    result = []
    for i in union:
        if i not in result:
            frequency = 0
            for j in union:
                if i == j:
                    frequency += 1
            if frequency == x:
                result.append(i)
    return result

print (frequency_x(2, [1,2,3], [2,3,4], [4,5,6], [7, 1, "test"]))