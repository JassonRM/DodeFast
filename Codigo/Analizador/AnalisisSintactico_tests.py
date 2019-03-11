import ply.yacc as yacc
from Codigo.Analizador.AnalisisLexico import tokens
# Get the token map from the lexer.  This is required.
# def p_exp(p):
#     '''expression : NUMBER'''
#     p[0]=p[1]
# def p_sum(p):
#     '''expression : expression PLUS expression
#                   | expression MINUS expression'''
#     p[0]=(p[2],p[1],p[3])
#     print("LOL")
#     print(p[0])
def p_inicio(p):
    '''expression : Inicio casos Final
    '''
    p[0]=(p[1],p[2],p[3])
    print(p[0])
def p_caso(p):
    ''' casos : EnCaso cuandos SiNo LKEY ID RKEY FinEnCaso SEMMICOLOM
    '''
    p[0] =(p[1],p[2],p[3],p[4],p[5],p[6],p[7])
def p_desigualdades(p):
    ''' desigualdades : EQUAL
    | GT
    | LT
    | GTE
    | LTE '''
    p[0] = p[1]
def p_cuandos(p):
    ''' cuandos : Cuando ID desigualdades NUMBER EnTons LKEY ID RKEY cuandos_primo
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7],p[8],p[9])
    print(p)
def p_cuandos_primos(p):
    '''
    cuandos_primo : epsilon
    | cuandos
    '''
    p[0]= p[1]
def p_epsilon(p):
    '''
    epsilon :
    '''
    p[0] = None
def p_declaracion(p):
    '''
    declaracion : DCL ID SEMMICOLOM declaracion_2
    | DCL ID DEFAULT NUMBER SEMMICOLOM declaracion_2
    '''
    if( len(p)==5):
        p[0]=(p[1],p[2],p[3],p[4])
    else:
        p[0]=(p[1],p[2],p[3],p[4],p[5],p[6])

def p_declaracion_2(p):
    '''
    declaracion_2 : declaracion
    | epsilon
    '''

    p[0]=p[1]
parser = yacc.yacc()
result = parser.parse("Inicio \n EnCaso \n Cuando \n juan < 12 EnTons \n { Maria } \n  SiNo \n {  MAMELA } \n FinEnCaso ; \n Final")
print("LOL")