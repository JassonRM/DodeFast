import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from Analizador.AnalisisLexico import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    print("mas")

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
    print("222")
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_statement5(p):
    'expression : ENCASO expression FINENCASO'
    p[0]= p[1] <<p[2] << p[3]
    print("s5")

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
result = parser.parse("ENCASO asasa FINENCASO")
print(result)