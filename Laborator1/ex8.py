'''
8. Given a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5")
and a number (int or float). Evaluate the polynomial for the given value.
'''

def polynomial_calculator(polynom, value):
    result = 0
    polynom = polynom.replace (" ", "")
    polynom = polynom.replace ("-", "+-")
    args = polynom.split("+")
    for arg in args:
        if arg == "":
            continue
        if arg[0] == '-':
            arg = arg.replace("-", "")
            if 'x' not in arg:
                result -= float(arg)
            else:
                parts = arg.split('x')
                if parts[1] == "":
                    result -= float(parts[0]) * value
                else:
                    result -= float(parts[0]) * (value ** int(parts[1][1:]))

        else:
            if 'x' not in arg:
                result += float(arg)
            else:
                parts = arg.split('x')
                if parts[1] == "":
                    result += float(parts[0]) * value
                else:
                    result += float(parts[0]) * (value ** int(parts[1][1:]))
    return result

print (polynomial_calculator("3x ^ 3 + 5x ^ 2 - 2x - 5.5", 1))
