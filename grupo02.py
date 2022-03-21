try:
    import ply.lex as lex
    import ply.yacc as yacc        
except ImportError:
    raise ImportError('Please, add ply library to the root of the proyect or run pip install -r requirements.txt')

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore whitespace
t_ignore = ' \t'

# Error handler
def t_error(t):
    print("Lex error. Character '%s' is not valid" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_OPERATION_AXIOM(p):
    '''OPERATION : OPERATION_NT OPERANDO_NT OPERATION_NT'''

def p_OPERATION(p):
    '''OPERATION_NT : LEFT_PARENTHESIS INTERNAL_OP RIGHT_PARENTHESIS
                    | INTERNAL_OP'''

def p_INTERNALOP(p):
     '''INTERNAL_OP : NUMBER OPERANDO NUMBER
                    | NUMBER OPERANDO OPERATION_NT
                    | OPERATION_NT OPERANDO NUMBER
                    | NUMBER'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")