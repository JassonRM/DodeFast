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
        self.argumentos
def listP(a):
    for i in range(len(a)):
        print(a[i].name + a[i].value)

def pDesiguales(var, simbolo,comp):
    x=int(buscarVar(var).value)
    if simbolo==">":
        return x>comp
    elif simbolo==">=":
        return x>=comp
    elif simbolo=="<":
        return x<comp
    elif simbolo=="<=":
        return x<=comp
    elif simbolo=="==":
        return x==comp
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
def addf(a,met):
    i=0
    while i<len(a):
        if a[i].name==var.name:
            print("REPETIDO")
            a[i].parametros=met.parametros
            a[i].cuerpo=met.cuerpo
            break
        i=i+1
    if i==len(a):
        a.append(met)
def buscarVar(x):
    y=None
    for i in range(len(variables)):
        if variables[i].name==x:
            y=variables[i]
            return y
    if y==None:
        print( "ERROR, Variable no encontrada")
variables.reverse()
funciones.reverse()