import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID','EQUAL', 'GT', 'LT', 'NE', 'GTE', 'LTE', 'PLUS', 'MINUS', 'TIMES',
          'DIVIDE', 'LPARENT', 'RPARENT','NUMBER','RKEY','LKEY',
          'SEMMICOLOM' ,'ASSIGN']
reservadas = ['DCL', 'EnCaso', 'Cuando', 'EnToncs', 'SiNo', 'Fin-EnCaso', 'Repita', 'HastaEncontrar', 'Desde', 'Hasta',
              'Haga', 'Fin-Desde', 'LLamar',
              'Inicio', 'Final', 'Proc']
t_ignore = '\t '
t_PLUS = r'\+'
t_ASSIGN = r'=='
t_LKEY=r'\{'
t_RKEY=r'\}'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
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
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_error(t):
    print('Caracter invalido' + t.value[0])
    t.lexer.skip(1)


def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t

analizador = lex.lex()
analizador.input('n==4;{}')

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)
