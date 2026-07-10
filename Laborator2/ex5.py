'''
5.	Sa se scrie o functie care primeste ca parametru o lista x, si un numar k. Sa se returneze o lista cu tuple care sa reprezinte combinari de len(x) luate cate k din lista x.
Exemplu: pentru lista x = [1,2,3,4] si k = 3 se va returna [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].
'''
def combinations (x, k):
    if k == 1:
        return x
    result =[]

    def backtracking(start, current):
        if len(current) == k:
            result.append(tuple(current))
            return
        else:
            for i in range(start, len(x)):
                current.append(x[i])
                backtracking(i + 1, current)
                del current[-1]

        return

    backtracking(0, [])
    return result

print (combinations([1,2,3,4], 3))
