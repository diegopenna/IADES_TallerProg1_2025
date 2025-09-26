
def mostrarMenu(itemsDeMenu:dict, titulo = "", pregunta = "Ingrese una Opcion...", error = "Opcion incorrecta..."):
    print()
    if (titulo != ""):
        print(titulo)

    for clave, valor in itemsDeMenu.items():
        print(f"{clave}) {valor}")
    
    valoresPosibles = itemsDeMenu.keys()
    while True:
        opc= input(pregunta)
        if opc in valoresPosibles:
            break
        else:
            print(error)
    return opc

def inputAnchoFijo(texto, ancho):
    while True:
        valor = input(texto)
        if (len(valor) != ancho):
            print("Error: El campo debe tener", ancho, "caracteres.")
        else:
            return valor 

def inputAnchoMaximo(texto, ancho):
    while True:
        valor = input(texto)
        if (len(valor) > ancho):
            print("Error: El campo debe tener un maximo de", ancho, "caracteres.")
        else:
            return valor 

def inputOpciones(texto, opciones:list):
    print(texto)
    valoresPosibles = []
    for i in range(len(opciones)):
        print(f"{i + 1}) {opciones[i]}")
        valoresPosibles.append(str(i+1))
    #print(valoresPosibles)
    while True:
        valor = input("Ingrese una opcion...")
        if valor not in valoresPosibles:
            print("Error: Debe elegir una opcion correcta.")
        else:
            return opciones[int(valor) - 1]

def inputFloat(texto, validaPositivo:bool, permiteCero:bool):
    while True:
        try:
            valor = float(input(texto))
            if (valor < 0):
                if (validaPositivo):
                    print("Error: El valor debe ser positivo.")
                else:
                    return valor
            elif (valor == 0):
                if (permiteCero == False):
                    print("Error: El valor no puede ser Cero.")
                else:
                    return valor
            else:
                return valor
        except (ValueError):
            print("Error: El valor tiene que ser un numero valido.")



def inputInt(texto, validaPositivo:bool, permiteCero:bool): 
    while True:   
        valor = inputFloat(texto, validaPositivo, permiteCero)
        if ((valor - int(valor)) == 0):
            return int(valor)
        else:
            print("Error: El valor tiene que se entero.")