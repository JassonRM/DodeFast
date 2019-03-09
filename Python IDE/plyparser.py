import ply.lex as lex

#Tokens a utilizar
tokens=(
    'INT',
    'DCL',
    'IGUAL',
    'MAS',
    'MENOS',
    'MULTIPLICAR',
    'DIVIDIR',
    'MAYOR',
    'MENOR',
    'DISTINTO',
    'MAYOROIGUAL',
    'MENOROIGUAL',
    'ENCASO',
    'FINENCASO',
    'CUANDO',
    'ENTONS',
    'SINO',
    'REPITA',
    'HASTAENCONTRAR',
    'DESDE',
    'HASTA',
    'HAGA',
    'FINDESDE',
    'INICIO',
    'FINAL',
    'PROC',
    'PARENI',
    'PAREND',
    'DEFAULT',
    'ID',
    'SEMICOLON',
    'LLAVEI',
    'LLAVED',
    'LLAMAR'
)

#REGEX para tokens simples
t_IGUAL = r'\='
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'\/'
t_DISTINTO = r'<>'
t_MAYOROIGUAL = r'>='
t_MENOROIGUAL = r'<='
t_MAYOR = r'>'
t_MENOR = r'<'
t_PARENI = r'\('
t_PAREND = r'\)'
t_SEMICOLON = r';'
t_DCL = r'DCL'
t_DEFAULT = r'DEFAULT'
t_LLAVEI = r'{'
t_LLAVED = r'}'
t_ENCASO = r'EnCaso'
t_FINENCASO = r'Fin-EnCaso'
t_CUANDO = r'Cuando'
t_ENTONS = r'Entons'
t_SINO = r'SiNo'
t_REPITA = r'Repita'
t_HASTAENCONTRAR = r'HastaEncontrar'
t_DESDE = r'Desde'
t_HASTA = r'Hasta'
t_HAGA = r'Haga'
t_FINDESDE = r'Fin-Desde'
t_INICIO = r'Inicio' #No se si incluir los dos puntos aqui o aparte
t_FINAL = r'Final'
t_PROC = r'Proc'
t_LLAMAR = r'Llamar'







#REGEX tokens complejos

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Simbolo prohibido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'([a-zA-Z_])([0-9a-zA-Z@_\#])*'
    return t

lexer = lex.lex()

def start(data):
    # Give the lexer some input
    lexer.input(data)

    toks = []
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        toks.append(tok)
    return toks