import ply.yacc as yacc
precedence=(
    ('right','ASSIGN'),
    ('right','EQUAL'),
    ('left','NE'),
    ('left','LT','LTE','GT','GTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','LPARENT','RPARENT'),
    ('left','RKEY','LKEY'))
def p_program(p):
    '''program : block'''
def p_DCLDecl(p):
    '''DCLDecl : DCL ID ;'''
    print("DCLDecl")
def p_empty(p):
    '''empty : '''
    pass
def p_error(p):
    print("Error de Sintaxis")
    print("Rrror en la linea: "+str(p.lineno))
parser = yacc.yacc()
result = parser.parse("DCL d=3")
print(result)