'''
3.	Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian. Sa se scrie o functie care primeste ca parametru
o lista de puncte si returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele unice determinate de acele puncte
( (a,b,c) corespunde dreptei ax + by + c = 0).
'''
def get_line(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    return a, b, c

def cmmdc (number1, number2):
    while number2:
        rest = number1 % number2
        number1 = number2
        number2 = rest
    return number1

def refactorize(a, b, c):
    divide_number = cmmdc(abs(a),cmmdc(abs(b),abs(c)))
    a //= divide_number
    b //= divide_number
    c //= divide_number

    if a < 0:
        a = -a
        b = -b
        c = -c
    elif a == 0 and b < 0:
        b = -b
        c = -c
    elif a == 0 and b == 0 and c < 0:
        c = -c
    return a, b, c
def get_all_unique_lines (points):
    lines = []
    for i in range (0, len(points) - 1):
        for j in range (i + 1, len(points)):
            a, b, c = get_line(points[i], points[j])
            line = refactorize(a, b, c)
            if line not in lines:
                lines.append(line)
    return lines

print (get_all_unique_lines([(0, 0), (1, 1), (2, 2), (3, 3)]))