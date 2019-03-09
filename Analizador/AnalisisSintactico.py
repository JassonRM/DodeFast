import ply.yacc as yacc
import os
import codecs
import re
from Analizador.AnalisisLexico import tokens
from sys import stdin
precedence=(
    ('right','ASSIGN'),
    ('right','EQUAL'),
    ('left','NE'),
    ('left','LT','LTE','GT','GTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','LPARENT','RPARENT'),
    ('left','RKEY','LKEY'))
def p_DCLDecl(p):
    'DCLDecl : DCL ID'
def p_DCLDeclEmpty(p):
    'DCLDecl : empty'
    #p[0]=Null()
    print("Nulo")
def p_identList1(p):
    'identlist : ID'
    print("ID1")
def p_identList2(p):
    'identList : identList ID'
    print("ID2")
def p_procDecl(p):
    'procDecl : procDecl Proc ID  '
    print("proc")
def p_procDelEmpty(p):
    '  procDecl : empty  '
    print("nulo")
def p_statement(p):
    'statement : ID ASSIGN expression'
    print("s1")
def p_statement2(p):
    ' statement : Llamar ID'
    print("s2")
def p_statement3(p):
    'statement : Inicio statementList Final'
    print("s3")
def p_statement4(p):
    'statement : Cuando  ID condition EnToncs LKEY statementList RKEY'
def p_statement41(p):
    'statement : Cuando condition EnToncs LKEY statementList RKEY'
def p_statement5(p):
    'statement : EnCaso statementList Fin_EnCaso'
    print("s5")
def p_statement11(p):
    'statement : EnCaso ID statementList Fin_EnCaso'
    print("s5")
def p_statement7(p):
    'statement : Repita statementList HastaEncontrar condition'
def p_statement8(p):
    'statement : Desde DCL Hasta condition Haga statementList Fin_Desde'
def p_statementEmpty(p):
    'statement : empty'
def p_statementList1(p):
    'statementList : statement'
def p_statementList2(p):
    'statement : statementList statement'
def p_condition(p):
    'condition : expression relation expression'
def p_relation1(p):
    'relation : ASSIGN'
def p_relation(p):
    'relation : NE'
def p_relation2(p):
    'relation : EQUAL'
def p_relation3(p):
    'relation : LT'
def p_relation4(p):
    'relation : GT'
def p_relation5(p):
    'relation : LTE'
def p_relation6(p):
    'relation : GTE'
def p_expression1(p):
    'expression : term'
def p_expression2(p):
    'expression : addingOperator term'
def p_expression3(p):
    'expression : expression addingOperator term'
def p_term1(p):
    'term : factor'
def p_term2(p):
    'term : term multiplyingOperator factor'
def p_multiplyingOperator(p):
    'multiplyingOperator : TIMES'
def p_multiplyingOperator2(p):
    'multiplyingOperator : DIVIDE'
def p_factor(p):
    'factor : ID'
def p_factor2(p):
    'factor : NUMBER'
def p_factor3(p):
    'factor : LPARENT expression RPARENT'
def p_empty(p):
    'empty : '
    pass
def p_error(p):
    print("Error de Sintaxis")
    print("Rrror en la linea: "+str(p.lineno))
parser = yacc.yacc()
result = parser.parse("DCL d=3")
print(result)