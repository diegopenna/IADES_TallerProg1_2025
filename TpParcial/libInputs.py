
def mostrarMenu(itemsDeMenu:dict, titulo = "", pregunta = "Ingrese una Opcion...", error = "Opcion incorrecta..."): 
    """
    Muestra un menu por consola y devuelve la opcion elegida.
    Args:
        itemsDeMenu (dict): Diccionario con las opciones del menu. La clave es el valor a devolver y el valor es la descripcion.
        titulo (str, optional): Titulo del menu. Defaults to "".
        pregunta (str, optional): Pregunta para elegir una opcion. Defaults to "Ingrese una Opcion...".
        error (str, optional): Mensaje de error para opcion incorrecta. Defaults to "Opcion incorrecta...".

    Returns:
        str: Clave del diccionario elegida por el usuario.
    
    Example:
        menu = {"1": "Opcion 1", "2": "Opcion 2", "3": "Opcion 3"}
        opcion = mostrarMenu(menu, "Menu Principal", "Elija una opcion:", "Opcion no valida")
        print("Opcion elegida:", opcion)

    """
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

def inputAlfanuNumerico(texto, anchofijo = None):
   while True:
        if anchofijo != None:
            valor = inputAnchoFijo(texto, anchofijo)
        else:
            valor = input(texto)
        esAlfanumerico = True
        for c in valor:
            if not ('a' <=  str(c).lower() <= 'z' or '0' <=  str(c).lower() <= '9'):
                print("Error: El campo solo acepta caracteres alfanumericos.")
                esAlfanumerico = False
                break
        if esAlfanumerico:
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