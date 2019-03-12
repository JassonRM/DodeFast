import ply.lex as lex
reservadas=['DCL', 'EnCaso', 'Cuando','EnTons', 'SiNo', 'FINENCASO', 'Repita', 'HastaEncontrar', 'Desde', 'Hasta',
              'Haga', 'FINDESDE', 'Llamar','Inicio', 'Final', 'Proc','DEFAULT','COMA','DPUNTO','MOVER','INC','INI','ALEATORIO','DEC']
movimientos=['AF','A','F','DFA','IFA','DFB','IFB','DAA', 'IAA','DAB','IAB','AA']
tokens = movimientos+reservadas+['ID','EQUAL', 'GT', 'LT', 'NE', 'GTE', 'LTE', 'PLUS', 'MINUS', 'TIMES',
          'DIVIDE', 'LPARENT', 'RPARENT','NUMBER','RKEY','LKEY','SEMMICOLOM' ,'ASSIGN']
t_ignore = '\t '
t_PLUS = r'\+'
t_ASSIGN = r'='
t_LKEY=r'\{'
t_RKEY=r'\}'
t_COMA=r','
t_DPUNTO=r':'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'=='
t_GT = r'>'
t_LT = r'<'
t_NE = r'<>'
t_GTE = r'>='
t_LTE = r'<='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_SEMMICOLOM = r';'
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
    print('Caracter invalido ' + t.value[0])
    t.lexer.skip(1)
def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t
analizador = lex.lex()
analizador.input("Inicio \n EnCaso \n Cuando \n juan < 12 EnTons \n { } \n  SiNo \n {  DCL D; } \n Fin-EnCaso ; \n Final")

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)