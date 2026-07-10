'''
1*. In cazul sirului Fibonacci fiecare termen este suma precedentilor 2.
Sa se scrie o functie care ia ca parametru 2 numere intregi, num_terms, n.
Num_terms va indica cati termeni vor fi calculati din urmatorul sir.
Sirul este asemanator Fibonacci cu mentiunea ca fiecare termen este suma ultimilor n termeni.
Sirul initial este format din n-1 0-uri si un 1. (e.g. n=5 sirul initial este 0 0 0 0 1)
'''
def fibonnacci_extended (num_terms, n):
    fib_list = []
    for i in range (1, n):
        fib_list.append(0)
    fib_list.append(1)
    if num_terms <= n:
        return fib_list[:num_terms]
    count = len(fib_list)
    while count < num_terms:
        fib_list.append(sum(fib_list[count - n: count]))
        count = count + 1
    return fib_list

print (fibonnacci_extended(10, 5))
