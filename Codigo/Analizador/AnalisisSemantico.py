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
def listvar(a):
    for i in range(len(a)):
        print(a[i].name + str(a[i].value))
def listMet(a):
    for i in range(len(a)):
        print(a[i].parametros )
def contParametros(a):
    i=0
    if len(a)>0:
        i=i+1
    for x in range(len(a)):
        if a[x]==",":
            i=i+1
    return i
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
        if a[i].name==met.name:
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
def buscarMetodos(x):
    y = None
    for i in range(len(funciones)):
        if funciones[i].name == x:
            y = funciones[i]
            return y
    if y == None:
        print("ERROR, Metodo no encontrada")
print(str(contParametros("qasa,xasa,e")))