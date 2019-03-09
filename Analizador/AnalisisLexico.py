import ply.lex as lex
reservadas=['DCL', 'ENCASO', 'CUANDO','ENTONCS', 'SINO', 'FINENCASO', 'REPITA', 'HASTAENCONTRAR', 'DESDE', 'HASTA',
              'HAGA', 'FINDESDE', 'LLAMAR','INICIO', 'FINAL', 'PROC','AF','A','F','DFA','IFA','DFB','IFB','DAA',
            'IAA','DAB','IAB','AA','DEFAULT']
tokens = reservadas+['ID','EQUAL', 'GT', 'LT', 'NE', 'GTE', 'LTE', 'PLUS', 'MINUS', 'TIMES',
          'DIVIDE', 'LPARENT', 'RPARENT','NUMBER','RKEY','LKEY',
          'SEMMICOLOM' ,'ASSIGN']
t_ignore = '\t '
t_PLUS = r'\+'
t_ASSIGN = r'='
t_LKEY=r'\{'
t_RKEY=r'\}'
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
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_#@]*'
    if t.value=='Fin-Desde':
        t.value='FINDESDE'
        t.type = t.value
    elif t.value=='Fin-EnCaso':
        t.value='FINENCASO'
        t.type = t.value
    elif t.value.upper() in reservadas:
        t.value=t.value.upper()
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
analizador.input('n==4;{}EnCaso Hasta Fin-Desde AF asas DEFAULT /     ')

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)