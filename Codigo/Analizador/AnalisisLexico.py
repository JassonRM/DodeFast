import ply.lex as lex
reservadas=['DCL', 'EnCaso', 'Cuando','EnTons', 'SiNo', 'FINENCASO', 'Repita', 'HastaEncontrar', 'Desde', 'Hasta',
              'Haga', 'FINDESDE', 'Llamar','Inicio', 'Final', 'Proc','DEFAULT','COMA','DPUNTO','MOVER','INC','INI','ALEATORIO','DEC']
movimientos=['AF','A','F','DFA','IFA','DFB','IFB','DAA', 'IAA','DAB','IAB','AA',"NONE"]
tokens = movimientos+reservadas+['ID','EQUAL', 'GT', 'LT', 'NE', 'GTE', 'LTE', 'PLUS', 'MINUS', 'TIMES',
          'DIVIDE', 'LPARENT', 'RPARENT','NUMBER','RKEY','LKEY','SEMMICOLOM' ]
t_ignore = '\t '
error = (False,[])
t_PLUS = r'\+'
t_EQUAL = r'='
t_LKEY=r'\{'
t_RKEY=r'\}'
t_COMA=r','
t_DPUNTO=r':'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GT = r'>'
t_LT = r'<'
t_NE = r'<>'
t_GTE = r'>='
t_LTE = r'<='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_SEMMICOLOM = r';'
def t_Llamar(t):
    r'Llamar'
    t.value='Llamar'
    t.type='Llamar'
    return t
# def t_A(t):
#     r'A'
#     t.value = 'A'
#     t.type = 'A'
#     return t
# # def t_F(t):
# #     r'F'
# #     t.value = 'F'
# #     t.type = 'F'
# #     return t
# def t_DFA(t):
#     r'DFA'
#     t.value = 'DFA'
#     t.type = 'DFA'
#     return t
# def t_IFA(t):
#     r'IFA'
#     t.value = 'IFA'
#     t.type = 'IFA'
#     return t
# def t_DFB(t):
#     r'DFB'
#     t.value = 'DFB'
#     t.type = 'DFB'
#     return t
# def t_IFB(t):
#     r'IFB'
#     t.value = 'IFB'
#     t.type = 'IFB'
#     return t
# def t_DAA(t):
#     r'DAA'
#     t.value = 'DAA'
#     t.type = 'DAA'
#     return t
# def t_AF(t):
#     r'AF'
#     t.value='AF'
#     t.type='AF'
#     return t


# def t_IAA(t):
#     r'IAA'
#     t.value='IAA'
#     t.type='IAA'
#     return t
# def t_DAB(t):
#     r'DAB'
#     t.value='DAB'
#     t.type='DAB'
#     return t
# def t_IAB(t):
#     r'IAB'
#     t.value='IAB'
#     t.type='IAB'
#     return t
# def t_AA(t):
#     r'AA'
#     t.value='AA'
#     t.type='AA'
#     return t
def t_HastaEncontrar(t):
    r'HastaEncontrar'
    t.value = "HastaEncontrar"
    t.type = "HastaEncontrar"
    return t
def t_Proc(t):
    r'Proc'
    t.value='Proc'
    t.type='Proc'
    return t
def Repita(t):
    r'Repita'
    t.value = "Repita"
    t.type = "Repita"
    return t
def t_Hasta(t):
    r'Hasta'
    t.value = "Hasta"
    t.type = "Hasta"
    return t
def t_Desde(t):
    r'Desde'
    t.value = "Desde"
    t.type = "Desde"
    return t
def t_Haga(t):
    r'Haga'
    t.value = "Haga"
    t.type = "Haga"
    return t

def t_FinEnCaso(t):
    r'Fin-EnCaso'
    t.value = "FINENCASO"
    t.type = "FINENCASO"
    return t
def t_EnCaso(t):
    r'EnCaso'
    t.value = "EnCaso"
    t.type = "EnCaso"
    return t
def t_Final(t):
    r'Final'
    t.value = "Final"
    t.type = "Final"
    return t
def t_SiNo(t):
    r'SiNo'
    t.value = "SiNo"
    t.type = "SiNo"
    return t
def t_EnTons(t):
    r'EnTons'
    t.value = "EnTons"
    t.type = "EnTons"
    return t

def t_Cuando(t):
    r'Cuando'
    t.value = "Cuando"
    t.type = "Cuando"
    return t
def t_Inicio(t):
    r'Inicio'
    t.value = "Inicio"
    t.type = "Inicio"
    return t
def t_Ini(t):
    r'Ini'
    t.value = "INI"
    t.type = "INI"
    return t
def t_Inc(t):
    r'Inc'
    t.value = "INC"
    t.type = "INC"
    return t
def t_Mover(t):
    r'Mover'
    t.value = "MOVER"
    t.type = "MOVER"
    return t
def t_Dec(t):
    r'Dec'
    t.value = "DEC"
    t.type = "DEC"
    return t
def t_Aleatorio(t):
    r'Aleatorio'
    t.value = "ALEATORIO"
    t.type = "ALEATORIO"
    return t
def t_FinDesde(t):
    r'Fin-Desde'
    t.value = "FINDESDE"
    t.type = "FINDESDE"
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_#@]*'
    if t.value in reservadas:
        t.type = t.value
    return t
def t_error(t):
    global error
    print('CARACTER INVALIDO' + t.value[0])
    error = (True,t.value[0])
    print(error)
    t.lexer.skip(1)
def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_NUMBER(t):
    r'[0-9]+'
    t.value=int(t.value)
    return t
def analizar(text):
    global error
    error = (False, [])
    analizador = lex.lex()
    analizador.input(text)
    print (analizador)
    while True:
        tok = analizador.token()
        if not tok : break
        print(tok)
    return error
