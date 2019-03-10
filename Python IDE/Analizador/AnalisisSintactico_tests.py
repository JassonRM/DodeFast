import ply.yacc as yacc

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
    ''' casos : EnCaso cuandos SiNo LKEY ID RKEY Fin_EnCaso SEMMICOLOM
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
parser = yacc.yacc()

# while True:
    #try:
      #  s = raw_input('1+1 ')
    # except EOFError:
    #     break
    #if not s: continue
result = parser.parse("Inicio \n EnCaso \n Cuando \n juan < 12 EnTons \n { Maria } \n Cuando \n Mario < 12 EnTons \n { Juana }\n SiNo \n {  MAMELA } \n Fin_EnCaso ; \n Final")
print("LOL")
