from Analizador.direction_creator import *
from Analizador.AnalisisSintactico_tests import result,procedimientos
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
        self.parametros=None
        self.variables=[]
        self.cuerpo=None
def parseProc(tupla):
    print(tupla)
    if isinstance(tupla, int):
        return None
    elif tupla == None:
        return None
    for i in range(len(tupla)):
        if isinstance(tupla[i], tuple):
            parseProc(tupla[i])
        elif tupla[i]=="Proc":
            print("INICIO DE PROCEDIMIENTO")
            procedi=metodos()
            procedi.name=tupla[1]
            procedi.parametros=tupla[3]
            procedi.cuerpo = (tupla[5],tupla[8])
            addfunc(procedi)
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
        print("Numero de parametros: "+str(contParametros(a[i].parametros )))
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
def parseLlama(proc,arg):
    args=[]
    lista = proc.parametros
    name = ""
    if contParametros(proc.parametros )== 1:
        for i in range(len(lista)):
            name += lista[i]
        x = var()
        x.name = name
        proc.variables.append(x)
        variables.append(x)
    elif contParametros(proc.parametros )> 0:
        for i in range(len(lista)):
            if lista[i] != ",":
                name += lista[i]
            else:
                x = var()
                x.name = name
                proc.variables.append(x)
                variables.append(x)
                name = ""
    name=""
    if contParametros(proc.parametros ) == 1:
        for i in range(len(arg)):
            name += arg[i]
        args.append(buscarVar(name))
    elif contParametros(proc.parametros ) > 0:
        for i in range(len(arg)):
            if arg[i] != ",":
                name += arg[i]
            else:
                args.append(buscarVar(name))
                name = ""
    for i in range(len(args)):
        proc.variables[i].value=args[i].value
    ejecutar(proc.cuerpo)
    for i in range(len(args)):
        args[i].value=proc.variables[i].value
    for i in range(len(proc.variables)):
        delete_var(proc.variables[i])
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
        elif tupla[i] == 'Repita':
            parse_repita(tupla)
        elif tupla[i] == 'Desde':
            parse_desde(tupla)
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
        elif tupla[i]=="Llamar":
            prod=buscarMetodos(tupla[1])
            agr=tupla[3]
            parseLlama(prod,agr)
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
parseProc(procedimientos)
ejecutar(result)
print("LISTA DE VARIABLES")
listvar(variables)
print("LISTA DE PROCEDIMIENTOS")
listMet(funciones)
