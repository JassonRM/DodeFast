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
    'PAREND'
)

#REGEX para tokens simples
t_IGUAL = r'\='
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'\/'
t_PARENI = r'\('
t_PAREND = r'\)'


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


lexer = lex.lex()

def start(data):
    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)