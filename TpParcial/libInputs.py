
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
