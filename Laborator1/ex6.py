'''
6. Write a function that converts a string of characters written in UpperCamelCase into snake_case
'''

def convert_style(camel_case_string):
    snake_case_string = camel_case_string[0].lower()
    for i in range(1, len(camel_case_string)):
        if camel_case_string[i].isupper():
            snake_case_string += '_' + camel_case_string[i].lower()
        else:
            snake_case_string += camel_case_string[i]

    return snake_case_string

print (convert_style('UpperCamelCase'))
