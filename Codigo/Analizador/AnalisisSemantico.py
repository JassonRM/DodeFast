from Analizador.AnalisisSintactico_tests import result,procedimientos
from Analizador.direction_creator import *
variables=[]
funciones=[]
instrucciones = Instructor()
class var:
    def __init__(self):
        self.value=0
        self.name=None
class metodos:
    def __init__(self):
        self.name=None
        self.num=0
        self.variables=[]
        self.cuerpo=None
def parseProc(tupla,fun):
    print(tupla)
    if isinstance(tupla, int):
        return None
    elif tupla == None:
        return None
    for i in range(len(tupla)):
        if isinstance(tupla[i], tuple):
            parseProc(tupla[i],None)
        elif tupla[i]=="Proc":
            print("INICIO DE PROCEDIMIENTO")
            procedi=metodos()
            procedi.name=tupla[i+1]
            procedi.num=contParametros(tupla[i+3])
            lista = tupla[i + 3]
            name =""
            if procedi.num==1:
                for i in range(len(lista)):
                    name += lista[i]
                x = var()
                x.name = name
                procedi.variables.append(x)
            elif procedi.num>0:
                for i in range(len(lista)):
                    if lista[i]!=",":
                        name+=lista[i]
                    else:
                        x=var()
                        x.name=name
                        procedi.variables.append(x)
                        name =""
            procedi.cuerpo = tupla[i+8]
            if tupla[i+5]!=None:
                aux=tupla[i+5]
                parseProc(aux,procedi)
            addfunc(procedi)
        elif tupla[i]=="DCL":
            if fun==None:
                return
            elif len(tupla)==4:
                variable=var()
                variable.name=tupla[1]
                variable.value=0
                addvar(variable,fun.variables)
            elif len(tupla)==6:
                variable = var()
                variable.name = tupla[1]
                variable.value = tupla[3]
                addvar(variable,fun.variables)
        elif tupla[i]=="Final":
            print("FINAL PROCEDIMIENTO")
def listvar(a):
    for i in range(len(a)):
        print("#################################")
        print("Variable: "+a[i].name )
        print("Valor: "+str(a[i].value))
def listMet(a):
    for i in range(len(a)):
        print("#################################")
        print("Procedimiento: "+a[i].name)
        print("Numero de parametros: "+str(a[i].num))
        print("Parametros: "+(str(a[i].variables)))
        print("Codigo: "+str(a[i].cuerpo))
def contParametros(a):
    i=0
    if len(a)>0:
        i=i+1
    for x in range(len(a)):
        if a[x]==",":
            i=i+1
    return i
def addfunc(proc):
    i = True
    for x in range(len(funciones)):
        if funciones[x].name == proc.name:
            i = False
            print("PROCEDIMIENTO YA EXISTENTE")
            break
    if i:
        print("PROCEDIMIENTO AGREGADA")
        funciones.append(proc)
def addvar(a,list):
    i=True
    for x in range(len(list)):
        if list[x].name==a.name:
            i=False
            print("VARIABLE YA EXISTENTE")
            break
    if i:
        print("VARIABLE AGREGADA")
        list.append(a)
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
    for i in range(len(tupla)):
        if isinstance(tupla[i], tuple):
            ejecutar(tupla[i])
        elif tupla[i]=="Inicio":
            print("INICIO DE CODIGO")
        elif tupla[i]=="DCL":
            if len(tupla)==4:
                variable=var()
                variable.name=tupla[1]
                variable.value=0
                addvar(variable,variables)
            elif len(tupla)==6:
                variable = var()
                variable.name = tupla[1]
                variable.value = tupla[3]
                addvar(variable,variables)
        elif tupla[i]=="EnCaso":
           print("ejecutar ENcaso"),
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
def check_cycle(tupla):
    var=False
    for i in range (len(tupla)):
        if(isinstance(tuple,tupla[i])):
            return check_cycle(tuple)
        elif (tupla[0]=='Inc' or tupla[0]=='Dec' or tupla[0]=='Ini'):
            return True
    return var

def parse_repita(tupla):
    if(check_cycle(tupla)):
        print("No tiene aumentos,disminuciones ni cambios a la variable, puede ser infinita")
    recursiones = 0
    while( pDesiguales(tupla[3], tupla[4], tupla[5])):
        recursiones+=1
        ejecutar(tupla[1])
        if(recursiones==3000):
            print("Posible Ciclo")
def parse_desde(tupla):
    variable = var()
    variable.name = tupla[1]
    variable.value = tupla[4]
    addvar(variable)
    while (pDesiguales(tupla[6], tupla[7], tupla[8])):
        ejecutar(tupla[9])
        incrementar(variable.name,1)
    delete_var(variable)
def delete_var(variable):
    variables.remove(variable)

parseProc(procedimientos,None)
ejecutar(result)
print(procedimientos)
print("LISTA DE VARIABLES")
listvar(variables)
print("LISTA DE PROCEDIMIENTOS")
listMet(funciones)
