from Analizador.AnalisisSintactico_tests import result
from Analizador.direction_creator import *
variables=[]
funciones=[]
instrucciones = Instructor()
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
def addvar(a):
    i=True
    for x in range(len(variables)):
        if variables[x].name==a.name:
            i=False
            print("VARIABLE YA EXISTENTE")
            break
    if i:
        print("VARIABLE AGREGADA")
        variables.append(a)
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
def incrementar(var,num):
    x=buscarVar(var)
    x.value+=num
def decrementar(var,num):
    x=buscarVar(var)
    x.value-=num
def iniciar(var,num):
    x=buscarVar(var)
    x.value=num
def ejecutar(tupla):
    print(tupla)
    if isinstance(tupla, int):
        return None
    elif tupla == None:
        return None
    for i in range(len(tupla)-1):
        if isinstance(tupla[i], tuple):
            ejecutar(tupla[i])
        elif tupla[i]=="Inicio":
            print("INICIO DE CODIGO")
        elif tupla[i]=="DCL":
            if len(tupla)==4:
                variable=var()
                variable.name=tupla[1]
                variable.value=0
                addvar(variable)
            elif len(tupla)==6:
                variable = var()
                variable.name = tupla[1]
                variable.value = tupla[3]
                addvar(variable)
        elif tupla[i]=="EnCaso":
           print("ejecutar ENcaso")
        elif tupla[i] == 'Mover':
            instrucciones.parsear_intruccion(tupla)
        elif tupla[i]=="Cuando":
            condicion=pDesiguales(tupla[1],tupla[2],tupla[3])
            if condicion:
                ejecutar("Cuando")
        elif tupla[i]=="INC":
            incrementar(tupla[2],int(tupla[4]))
        elif tupla[i]=="INI":
            iniciar(tupla[2],int(tupla[4]))
        elif tupla[i]=="DEC":
            decrementar(tupla[2],int(tupla[4]))
        elif tupla[i]=="Final":
            print("FIN DE CODIGO")
ejecutar(result)
listvar(variables)
