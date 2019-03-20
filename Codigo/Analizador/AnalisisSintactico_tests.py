import ply.yacc as yacc
from Analizador.AnalisisLexico import tokens
def p_inicio(p):
    '''expression : Inicio declaracion sentencias Final procedimiento
    '''
    p[0]=(p[1],p[2],p[3],p[4],p[5])
def p_caso(p):
    ''' casos : EnCaso cuandos SiNo LKEY sentencias RKEY FINENCASO SEMMICOLOM sentencias
    | EnCaso ID cuandos_5 SiNo LKEY sentencias RKEY FINENCASO SEMMICOLOM sentencias
    '''
    if len(p)==9:
        p[0] =(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
    else:
        p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])
def p_desigualdades(p):
    ''' desigualdades : EQUAL
    | GT
    | LT
    | GTE
    | LTE '''
    p[0] = p[1]

def p_cuandos(p):
    ''' cuandos : Cuando ID desigualdades NUMBER EnTons LKEY sentencias RKEY cuandos_primo
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7],p[8],p[9])
def p_cuandos_5(p):
    '''
    cuandos_5 : Cuando  desigualdades NUMBER EnTons LKEY sentencias RKEY cuandos_5
    | epsilon
    '''
    if(len(p)==9):
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    else:
        p[0]=p[1]
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
def p_idopcional(p):
    '''
    idopcional : ID
    | epsilon
    '''
    p[0]=p[1]
#No me sirve jaja, y hay que probarlo para todos los casos donde no hay parametros y asi
#AUN FATLTA
def p_procedimiento(p):
    '''
    procedimiento : Proc ID LPARENT idopcional RPARENT  declaracion_2 Inicio DPUNTO sentencias Final SEMMICOLOM procedimiento
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
    | DEC LPARENT ID COMA NUMBER RPARENT
    | INI LPARENT ID COMA NUMBER RPARENT
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
def p_error(p):
    print("ERROR DE SINTAXIS: \n"+str(p)+"\nLINEA :"+str(p.lineno-8))
parser = yacc.yacc()
result = parser.parse("Inicio DCL juan DFAULT 100; DCL juan DEFAULT 10;\n EnCaso \n Cuando  \n juan > 12 EnTons \n {  } \n  SiNo \n {  } \n Fin-EnCaso ; \n  Final")
print(result)
