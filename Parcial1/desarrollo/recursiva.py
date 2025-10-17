def miFuncionRec(lista:list):
    lista = list(lista)
    cant = len(lista)
    if cant == 0:
        return
    valor = lista.pop(cant - 1)
    cadena = str(cant) + " - " + str(valor)
    miFuncionRec(lista)
    print(cadena)


colores = ["Rojo", "Amarillo", "Azul", "Blanco", "Negro"]
miFuncionRec(colores)
print(colores)
