import ply.yacc as yacc
from Codigo.Analizador.AnalisisLexico import tokens
def p_inicio(p):
    '''expression : Inicio declaracion sentencias Final
    '''
    p[0]=(p[1],p[2],p[3])
    print(p[0])
def p_caso(p):
    ''' casos : EnCaso cuandos SiNo LKEY declaracion RKEY FINENCASO SEMMICOLOM
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
    ''' cuandos : Cuando ID desigualdades NUMBER EnTons LKEY declaracion RKEY cuandos_primo
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

def p_procedimiento(p):
    '''
    procedimiento : Proc ID LPARENT ID RPARENT declaracion Inicio DPUNTO sentencias Final SEMMICOLOM procedimiento
    | epsilon
    '''
    if(len(p)>5):
        p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
    else:
        p[0]=p[1]
def p_repita(p):
    '''
    repeticion_R : Repita sentencias HastaEncontrar ID desigualdades NUMBER sentencias
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
def  p_repita_2(p):
    '''
    repita_2 : Desde ID DPUNTO EQUAL Hasta ID desigualdades sentencias FINDESDE sentencias
    '''
    p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10])
def p_funciones(p):
    '''
    funcion : matematicas sentencias
    | MOVER LPARENT movimiento RPARENT sentencias
    | ALEATORIO LPARENT RPARENT sentencias
    '''
    if(len(p)==3):
        p[0] = (p[1], p[2])
    elif( len(p)==4):
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5])
def p_argumento(p):
    '''
    argumento : ID COMA argumento
    | epsilon
    | ID
    '''
    if(len(p)==4):
        p[0]=(p[1],p[2],p[3])
    else:
        p[0] = p[1]
def p_llamada(p):
    '''
    llamadas : Llamar  ID LPARENT argumento  RPARENT SEMMICOLOM sentencias
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
def p_sentencia(p):
    '''
    sentencias : casos
    | llamadas
    | funcion
    | repeticion_R
    | repita_2
    | epsilon
    '''
    p[0] = p[1]
def p_mov(p):
    '''
    movimiento : AF
    | F
    | DFA
    | IFA
    |  DFB
    | IFB
    | A
    | DAA
    | IAA
    | DAB
    | IAB
    | AA
    '''
    p[0] = p[1]
def p_matematicas(p):
    '''
    matematicas : INC LPARENT ID COMA NUMBER RPARENT
    | Dec LPARENT ID COMA NUMBER RPARENT
    | Ini LPARENT ID COMA NUMBER RPARENT
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
parser = yacc.yacc()
result = parser.parse("Inicio DCL B DEFAULT 100; \n EnCaso \n Cuando \n juan < 12 EnTons \n { DCL C DEFAULT 3;DCL C DEFAULT 3;DCL C DEFAULT 3; } \n  SiNo \n {  DCL D; } \n Fin-EnCaso ; \n Final")
print("LOL")