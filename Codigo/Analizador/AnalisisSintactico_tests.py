import ply.yacc as yacc
from Analizador.AnalisisLexico import tokens
from  Analizador.AnalisisLexico import analizar
from Analizador.AnalisisSemantico import parseProc,ejecutar
parseo_aprobado = True
error=""
def p_inicio(p):
    '''expression : Inicio declaracion sentencias Final procedimiento
    '''
    p[0]=(p[1],p[2],p[3],p[4],p[5])
def p_casos(p):
    ''' casos : EnCaso cuandos SiNo LKEY sentencias RKEY FINENCASO SEMMICOLOM sentencias
    | EnCaso ID cuandos_5 SiNo LKEY sentencias RKEY FINENCASO SEMMICOLOM sentencias
    '''
    if len(p)==10:
        p[0] =((p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]),p[9])
    else:
        p[0] = ((p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]),p[10])
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
    procedimiento : Proc ID LPARENT argumento RPARENT  declaracion_2 Inicio DPUNTO sentencias Final SEMMICOLOM procedimiento
    | epsilon
    '''
    if(len(p)>5):
        p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
    else:
        p[0]=p[1]
def p_repita(p):
    '''
    repeticion_R : Repita sentencias HastaEncontrar ID desigualdades NUMBER  SEMMICOLOM sentencias
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7],p[8])
def  p_repita_2(p):
    '''
    repita_2 : Desde ID DPUNTO EQUAL NUMBER Hasta ID desigualdades NUMBER Haga sentencias FINDESDE sentencias
    '''
    p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13])
def p_funciones(p):
    '''
    funcion : matematicas sentencias
    | MOVER LPARENT movimiento RPARENT sentencias
    | ALEATORIO LPARENT RPARENT sentencias
    '''
    if(len(p)==3):
        p[0] = (p[1],p[2])
    elif( len(p)==5):
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
def p_llamadas(p):
    '''
    llamadas : Llamar  ID LPARENT argumento  RPARENT SEMMICOLOM sentencias
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
def p_sentencias(p):
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
    movimiento : ID
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
    global error
    error="Error de sintaxis:"+'\n'+str(p)+"\n LINEA :"+str(p.lineno-8)
    print("Error de sintaxis en : \n"+str(p)+"\n LINEA :"+str(p.lineno-8))
def purba(lolol):
    if lolol == 34:
        purba(1)
    else:
        print("LOL")
def parse_codigo(codigo):
    global error
    valor = analizar(codigo)
    parser = yacc.yacc()
    parseo = parser.parse(codigo)
    print(valor)
    if(valor[0]):
        return (False,valor[1])
    if (parseo == None):
        return [False,[error]]
    else:
        result_2 = parseo[0:4]
        procedimientos_2 = parseo[4]
        parseProc(procedimientos_2)
        resultado = ejecutar(result_2)
        return resultado

# purba(23)
# archivo = open("codigo.txt")
# test=archivo.read()
# archivo.close()
# print(parse_codigo(test))
# print(parse_codigo(test))
# parser = yacc.yacc()
#
# parseo= parser.parse(test)

