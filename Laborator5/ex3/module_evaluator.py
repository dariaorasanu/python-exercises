"""
3. Write a script that reads a file, line by line, and for every triple (a, b, c - separated by spaces) applies operator
c for the operands a and b. The valid operations are : +, *, -,  /, ** .
Input Example:
■	3 5 ** => 3 ** 5 =  243
■	7 2 + => 7 + 2   = 9
"""


def evaluate(input_file):
    try:
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                a, b, c = line.split()
                a = int(a)
                b = int(b)
                if c == '+':
                    print(f'{a} {c} {b} = {a + b}')
                elif c == '-':
                    print(f'{a} {c} {b} = {a - b}')
                elif c == '*':
                    print(f'{a} {c} {b} = {a * b}')
                elif c == '**':
                    print(f'{a} {c} {b} = {a ** b}')
                elif c == '/':
                    if b == 0:
                        raise ArithmeticError("Nu se poate efectua impartirea la 0")
                    else:
                        print(f'{a} {c} {b} = {a / b}')

    except OSError as e:
        print(f"Eroare la citirea din fisier: {str(e)}")
    except Exception as e:
        print(f"A aparut o alta eroare: {str(e)}")

