import re

# Initialization
stack = []
parenthesis_stack = []

def calculator(s):
    newString = s.replace(" ", "")
    tokens_list = list(newString)
    position = ''
    # Recorrer la lista para encontrar los **
    for idx, val in enumerate(tokens_list):
        if val == '*' and tokens_list[idx+1] == '*':
            print('potencia')
            ##reemplazar esa potencia por un solo carater que tenga **
            tokens_list.remove(val)
            tokens_list[idx] = '**'
    
    for token in tokens_list:
        if token == '(':
            parenthesis_stack.append(")")
        if token == ')':
            parenthesis_stack.remove(token)

    print(parenthesis_stack)
    return tokens_list
