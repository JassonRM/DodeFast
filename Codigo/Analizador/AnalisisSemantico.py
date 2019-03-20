from Analizador.AnalisisSintactico_tests import result
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
        print(a[i].name )
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
    elif simbolo=="=":
        return x==comp
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

def ejecutar(tupla):
    print(tupla)
    if isinstance(tupla, int):
        return None
    elif tupla == None:
        return None
    for i in range(len(tupla)-1):
        if tupla[0]=="Inicio":
            ejecutar(tupla[i+1])
        elif tupla[0]=="DCL":
            if len(tupla)==4:
                variable=var()
                variable.name=tupla[1]
                variable.value=0
                variables.append(variable)
            elif len(tupla)==6:
                variable = var()
                variable.name = tupla[1]
                variable.value = tupla[3]
                variables.append(variable)
            ejecutar(tupla[i+1])
        elif tupla[0]=="EnCaso":
            ejecutar(tupla[i+1])
        elif tupla[0]=="Cuando":
            condicion=pDesiguales(tupla[1],tupla[2],tupla[3])
            if condicion:
                print("CIERTO")
                ejecutar(tupla[6])
                break
            ejecutar(tupla[i+1])

ejecutar(result)