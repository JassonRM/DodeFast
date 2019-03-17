import ply.yacc as yacc
from Codigo.Analizador.AnalisisLexico import tokens
variables=[]
funciones=[]
class var:
    def __init__(self):
        self.value=None
        self.name=None
class metodos:
    def __init__(self):
        self.name=None
        self.parametros=None
        self.cuerpo=None
def addVar(a,var):
    i=0
    while i<len(a):
        if a[i].name==var.name:
            print("REPETIDO")
            a[i].value=var.value
            break
        i=i+1
    if i==len(a):
        a.append(var)
def p_inicio(p):
    '''expression : Inicio declaracion sentencias Final
    '''
    p[0]=(p[1],p[2],p[3])
def p_caso(p):
    ''' casos : EnCaso cuandos SiNo LKEY sentencias RKEY FINENCASO SEMMICOLOM
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
    ''' cuandos : Cuando ID desigualdades NUMBER EnTons LKEY sentencias RKEY cuandos_primo
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7],p[8],p[9])
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
    variable=var()
    if( len(p)==5):
        p[0]=(p[1],p[2],p[3],p[4])
        variable.value=str(0)
        variable.name=p[2]
    else:
        p[0]=(p[1],p[2],p[3],p[4],p[5],p[6])
        variable.name=p[2]
        variable.value=str(p[4])
    addVar(variables,variable)

def p_declaracion_2(p):
    '''
    declaracion_2 : declaracion
    | epsilon
    '''

    p[0]=p[1]
#No me sirve jaja, y hay que probarlo para todos los casos donde no hay parametros y asi
def p_procedimiento(p):
    '''
    procedimiento : Proc ID LPARENT ID RPARENT declaracion Inicio DPUNTO sentencias Final SEMMICOLOM procedimiento
    | epsilon
    '''
    met=metodos()
    if(len(p)>5):
        p[0] = (p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
        met.name=p[2]
        met.parametros=p[4]
        met.cuerpo=p[9]
    else:
        p[0]=p[1]
    funciones.append(met)
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
parser = yacc.yacc()
result = parser.parse("Inicio DCL A DEFAULT 12;\n DCL B;  \n DCL A;\n DCL A DEFAULT 23; \nDCL B DEFAULT 5;\n DCL D DEFAULT 21; EnCaso \n Cuando  \n juan < 12 EnTons \n {  } \n  SiNo \n {  } \n Fin-EnCaso ; \n Final")
variables.reverse()
def listP(a):
    for i in range(len(a)):
        print(a[i].name + a[i].value)

listP(variables)