import pathlib, os

listaActiva:list = None
nombreArchivo:str = None
modificada:bool = False

def menuInicial():
    while True:
        print("***********Abm de Listas************")
        print("1- Nueva")
        print("2- Abrir")
        print("3- Guardar")
        print("4- Guardar como...")
        print("----------------------")
        print(descripcionLista())
        print("5- Ver")
        print("6- Agregar elemento")
        print("7- Modificar elemento")
        print("8- Borrar elemento")
        print("----------------------")
        print("9- Salir")
        while True:
            opc = input("Ingrese una opcion:")
            if opc in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break

        if opc == "1":
            nuevaLista()
        elif opc == "2":
            if abrir():
                verLista()
        elif opc == "3":
            guardar()
        elif opc == "4":
            guardarComo()
        elif opc == "5":
            verLista()
        elif opc == "6":
            agregarElemento()
        elif opc == "7":
            print("7- Modificar elemento")
        elif opc == "8":
            print("8- Borrar elemento")
        elif opc == "9":
            break
        #input("\nPresione enter para continuar...")

def descripcionLista():
    if listaActiva == None:
        return "No hay lista Activa"
    
    if nombreArchivo == None:
        nombre = "Nueva Lista"
    else:
        nombre = nombreArchivo
    if modificada == True:
        nombre = "*" + nombre
    
    return "Lista activa: " + nombre

def nuevaLista():
    global listaActiva, modificada, nombreArchivo

    if validarListaModificada() == False:
        return False

    listaActiva = []
    nombreArchivo = None
    modificada = False
    print("✔ Se creo una nueva lista")
    return True

def validarListaActiva():
    if (listaActiva == None):
        input("⚠ Atención, no hay una Lista activa.\nPresione Enter para continuar...")
        return False
    else:
        return True

def validarListaModificada():
    if (modificada == True):
        print("⚠ Atención, existen cambios sin guardar en la lista actual.")
        opc = input("¿Desea continuar de todos modos? (s/n)")
        if (opc != "s"):
            return False
    return True

def agregarElemento():
    global modificada
    if not validarListaActiva():
        return False
    
    elemento = input("Ingrese un Elemento de lista")
    listaActiva.append(elemento.strip())
    modificada = True
    return True

def verLista():
    if not validarListaActiva():
        return False
    cont = 0
    print("\nDatos de la lista:")
    for elemento in listaActiva:
        cont += 1
        print(f"{cont}- {elemento}")

    input("\nPresione enter para continuar...")
    return True

def abrir():
    if not validarListaModificada():
        return False

    
    listaArch = []

    for arch in os.listdir():
        if (not pathlib.Path(arch).is_dir()):
            listaArch.append(arch)
    
    print("Seleccione la lista que desea abrir:")
    for i in range(len(listaArch)):
        print(f"{i + 1}) {listaArch[i]}")
    
    opc = int(input("Ingrese un numero:"))

    nombre = listaArch[opc - 1]
    nuevaLista = []
    with open(nombre, "r", encoding="utf8") as f:
        for linea in f:
            nuevaLista.append(linea.strip())

    global nombreArchivo, listaActiva, modificada
    nombreArchivo = nombre
    listaActiva = nuevaLista
    modificada = False
    return True


def guardar():
    if not validarListaActiva():
        return False
    
    if nombreArchivo == None:
        return guardarComo()
    
    with open(nombreArchivo, "w", encoding="utf8") as f: 
        for elemento in listaActiva:
            f.write(elemento + "\n")
    
    modificada = False
    print("Archivo guardado con Exito.")
    input("\nPresione enter para continuar...")
    return True



def guardarComo():
    global modificada, nombreArchivo
    if not validarListaActiva():
        return False
    nombre = input("Ingrese nombre del Archivo.")
    
    arch = pathlib.Path(nombre)
    if (arch.exists()):
        opc = input("El archivo ya existe.\n¿Esta seguro que desea continuar? s/n")
        if (opc != 's'):
            print("Operacion canelada por el usuario.")
            input("\nPresione enter para continuar...")
            return False

    #With .... as f reempaza el f = open .... f.close()#
    with open(nombre, "w", encoding="utf8") as f: 
        for elemento in listaActiva:
            f.write(elemento + "\n")
    
    modificada = False
    nombreArchivo = nombre
    print("Archivo guardado con Exito.")
    input("\nPresione enter para continuar...")
    return True



menuInicial()