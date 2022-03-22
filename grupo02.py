def calculator(s):
    newString = s.replace(" ", "")
    tokens_list = list(newString)
    val = ''
    idx = 0
    terminos = []
    posTerminos = []
    prioridades = []

    # Recorrer la lista para encontrar las potencias que son un caso especial **
    for idx, val in enumerate(tokens_list):
        if val == '*' and tokens_list[idx+1] == '*':
            ## reemplazar esa potencia por un solo carater que tenga ** **
            tokens_list.remove(val)
            tokens_list[idx] = '**'
    
    for idx, val in enumerate(tokens_list):
        if val == '(':
            prioridades.append(idx)
            posTerminos.append(idx)
        if val == ')':
            posUlt = posTerminos.pop()
            aux={}
            aux['tokens']= tokens_list[posUlt : idx + 1]
            terminos.append(aux)

    for idx, val in enumerate(terminos):
        cadena = ''.join(val['tokens'])
        terminos[idx]['result'] = eval(cadena)
    return (terminos[-1]['result'], ''.join(terminos[0]['tokens']).replace("(", "").replace(")", ""))