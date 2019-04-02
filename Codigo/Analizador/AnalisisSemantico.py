from Analizador.direction_creator import *
variables=[]
funciones=[]
Error=False
instrucciones = Instructor()
class var:
    def __init__(self):
        self.value=0
        self.name=None
class metodos:
    def __init__(self):
        self.name=None
        self.parametros=None
        self.cuerpo=None
        self.variables=[]
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
            for i in range(len(procedi.parametros)):
                if procedi.parametros[i] != ",":
                    vari = var()
                    vari.name = procedi.parametros[i]
                    procedi.variables.append(vari)
                    variables.append(vari)
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
    global Error
    global error
    i = True
    for x in range(len(funciones)):
        if funciones[x].name == proc.name:
            i = False
            print("PROCEDIMIENTO YA EXISTENTE")
            Error=True
            error="PROCEDIMIENTO "+proc.name+" YA EXISTE"

    if i:
        print("PROCEDIMIENTO AGREGADA")
        funciones.append(proc)
def addvar(a,list):
    global Error
    global error
    i=True
    for x in range(len(list)):
        if list[x].name==a.name:
            i=False
            print("VARIABLE YA EXISTENTE")
            Error=True
            error="VARIABLE " +a.name +" REPETIDA"

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
    global Error
    global error
    for i in range(len(variables)):
        if variables[i].name==x:
            y=variables[i]
            return y
    if y==None:
        print( "ERROR, Variable no encontrada")
        Error = True
        error="VARIABLE "+ x +" NO EXISTE"

def buscarMetodos(x):
    global error
    global Error
    y = None
    for i in range(len(funciones)):
        if funciones[i].name == x:
            y = funciones[i]
            return y
    if y == None:
        error= "ERROR, Metodo "+ x +" no encontrado"
        Error=True
        return y
def incrementar(var,num):
    print(var)
    x=buscarVar(var)
    x.value+=num
def decrementar(var,num):
    x=buscarVar(var)
    x.value-=num
def iniciar(var,num):
    x=buscarVar(var)
    x.value=num
def parseLlama(proc,args):
    para=[]
    if isinstance(args, str):
        para.append(buscarVar(args))
    else:
        for i in range(len(args)):
            if args[i]!=",":
                para.append(buscarVar(args[i]))
    for i in range(len(para)):
        proc.variables[i].value=para[i].value
    ejecutar(proc.cuerpo)
    for i in range(len(para)):
        para[i].value=proc.variables[i].value
    for i in range(len(proc.variables)):
        delete_var(proc.variables[i])
def parseEnCaso(tupla):
    condicion=True
    for i in range(len(tupla)):
        if isinstance(tupla[i], tuple):
            parseEnCaso(tupla[i])
        elif tupla[i]=="EnCaso":
            ejecutar(tupla[i])
        elif tupla[i]=="Cuando":
            valor=pDesiguales(tupla[1],tupla[2],tupla[3])
            if valor:
                condicion=False
                ejecutar(tupla[6])
        elif tupla[i]=="SiNo" and condicion:
            ejecutar(tupla[4])
def parseEnCaso2(var,tupla):
    condicion=True
    for i in range(len(tupla)):
        if isinstance(tupla[i], tuple):
            parseEnCaso2(var,tupla[i])
        elif tupla[i]=="EnCaso":
            ejecutar(tupla[i])
        elif tupla[i]=="Cuando":
            valor=pDesiguales(var,tupla[1],tupla[2])
            if valor:
                print("#"+str(tupla[5]))
                condicion=False
                ejecutar(tupla[5])
        elif tupla[i]=="SiNo" and condicion:
            ejecutar(tupla[5])
error = ""
def compare(x,v):
    return x==v
def ejecutar_aux(tupla):
    global variables
    global instrucciones
    global funciones
    variables=[]
    instrucciones.parseado = []
    funciones = []
    return ejecutar(tupla)
def ejecutar(tupla):
    global instrucciones
    global error
    global Error
    if not Error:
        print(tupla)
        if isinstance(tupla, int):
            return None
        elif tupla == None:
            return None
        for i in range(len(tupla)):
            if not Error:
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
                elif tupla[i] == 'MOVER':
                    if Error:
                        break
                    print("ENTRE AQUI")
                    Error=instrucciones.parsear_intruccion(tupla)
                    if Error:
                        error ="Error semantico, el argumento " + tupla[2]+" no es valido"
                        break
                elif tupla[i]=="INC":
                    incrementar(tupla[2],int(tupla[4]))
                elif tupla[i]=="INI":
                    iniciar(tupla[2],int(tupla[4]))
                elif tupla[i]=="DEC":
                    decrementar(tupla[2],int(tupla[4]))
                elif tupla[i]=="EnCaso":
                    if isinstance(tupla[1],tuple):
                        parseEnCaso(tupla[1])
                    else:
                        parseEnCaso2(tupla[1],tupla[2])
                    break
                elif tupla[i]=="Final":
                    print("FIN DE CODIGO")
                elif tupla[i]=="Llamar":
                    prod=buscarMetodos(tupla[1])
                    agr=tupla[3]
                    if prod==None:
                        Error=True
                        error="NO EXISTE EL PROCEDIMIENTO " + str(tupla[1])
                        break
                    cont1=contParametros(prod.parametros)
                    con2=contParametros(agr)
                    x=compare(cont1,con2)
                    if not x :
                        Error=True
                        error = "ERROR DE PARAMETROS EN " + str(tupla[1])
                        break
                    else:
                        parseLlama(prod,agr)
    return [ not Error,error,instrucciones.parseado]

def parse_repita(tupla):
    recursiones = 0
    while( not pDesiguales(tupla[3], tupla[4], tupla[5])):
        recursiones+=1
        ejecutar(tupla[1])
        if(recursiones==3000):
            print("Posible Ciclo")
def parse_desde(tupla):
    variable = var()
    variable.name = tupla[1]
    variable.value = tupla[4]
    addvar(variable,variables)
    while (pDesiguales(tupla[6], tupla[7], tupla[8])):
        print("ENTRE AQUI LELELELF")
        ejecutar(tupla[10])
        incrementar(variable.name,1)
    delete_var(variable)
def delete_var(variable):
    try:
        variables.remove(variable)
    except:
        print("")

for i in range(len(funciones)):
    for x in range(len(funciones[i].variables)):
        try:
            delete_var(funciones[i].variables[x])
        except:
            print("")



print("LISTA DE VARIABLES")
listvar(variables)
print("LISTA DE PROCEDIMIENTOS")
listMet(funciones)
print("RESULTADO INSTRUCCIONES")
print(instrucciones.parseado)