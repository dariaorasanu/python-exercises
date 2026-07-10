'''
8.	Sa se scrie o functie care primeste un numar variabil de liste si returneaza o lista de tuple astfel:
primul tuplu sa contina primele elemente din liste, al doilea element sa contina elementele de pe pozitia 2 din liste, etc.
Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"] se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")].
Observatie: In cazul in care listele primite ca input nu au acelasi numar de elemente, elementele lipsa vor fi inlocuite
cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple. Pe scurt: implementati zip! (fara sa folositi zip) 😊
'''

def zip_implementation (*lists):
    max_length = 0
    for l in lists:
        if len (l) > max_length:
            max_length = len(l)
    result = []
    for i in range (0, max_length):
        current_result = []
        for l in lists:
            if i >= len(l):
                current_result.append(None)
            else:
                current_result.append(l[i])
        result.append(current_result)

    return tuple(result)

print (zip_implementation([1,2,3], [5,6,7], ["a", "b", "c"]))