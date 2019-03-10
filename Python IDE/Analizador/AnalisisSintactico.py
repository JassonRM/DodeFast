import ply.yacc as yacc


def p_DCLDecl(p):
    'DCLDecl : DCL ID'
    print("DCL")
def p_DCLDeclEmpty(p):
    'DCLDecl : empty'
    print("Nulo")
def p_procDecl(p):
    'procDecl : procDecl PROC ID  '
    print("proc")
def p_procDelEmpty(p):
    'procDecl : empty'
    print("nulo")
def p_statement(p):
    'statement : ID ASSIGN expression'
    print("s1")
def p_statement2(p):
    ' statement : LLAMAR ID'
    print("s2")
def p_statement3(p):
    'statement : INICIO statement FINAL'
    print("s3")
def p_statement4(p):
    'statement : CUANDO ID condition ENTONCS LKEY statement RKEY'
def p_statement41(p):
    'statement : CUANDO condition ENTONCS LKEY statement RKEY'
def p_statement5(p):
    'statement : ENCASO statement FINENCASO'
    print("s5")
def p_statement11(p):
    'statement : ENCASO ID statement FINENCASO'
    print("s5")
def p_statement7(p):
    'statement : REPITA statement HASTAENCONTRAR condition'
def p_statement8(p):
    'statement : DESDE DCL HASTA condition HAGA statement FINDESDE'
def p_statementEmpty(p):
    'statement : empty'
def p_condition(p):
    'condition : expression relation expression'
def p_relation1(p):
    'relation : ASSIGN'
def p_relation(p):
    'relation : NE'
def p_relation2(p):
    'relation : EQUAL'
    print("igual")
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
def p_expression3(p):
    'expression : expression PLUS term'  #aqui generaba otro error ya que antes tenia plus algo y el comando de sumar es plus
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
    print("NUMBER")
def p_factor3(p):
    'factor : LPARENT expression RPARENT'
    print("22")
def p_empty(p):
    'empty : '
    pass
def p_error(p):
    print("Error de Sintaxis")
    print("Error en la linea: "+str(p.lineno))
parser = yacc.yacc()
parser.parse('(x=4)')
