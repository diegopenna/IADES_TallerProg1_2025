def mostrarMenu(*opciones, titulo):

    print(titulo)
    print()
    for i in range(len(opciones)):
        print(f"{i+1}: {opciones[i]}")
    opc = int(input("Ingrese una opcion..."))
    return opciones[opc - 1]



def mostrarMenu2(titulo, *opciones, textopie = "Ingrese un valor..."):

    print(titulo)
    print()
    for i in range(len(opciones)):
        print(f"{i+1}: {opciones[i]}")
    
    if (len(opciones) > 0):
        opc = int(input(textopie))
        return opciones[opc - 1]


opc = mostrarMenu("Alta", "Baja", "Modificacion", "Listar Resultados", "Exportar", titulo="Menu de opciones")
print("Opcion elegida:", opc)

print("+++++++++++++++++++++")
opc = mostrarMenu2("Segundo Menu de opciones", "Alta", "Baja", "Modificacion", "Listar Resultados", "Exportar",textopie= "Escribí un numero:")
print("Opcion elegida 2:", opc)

print("+++++++++++++++++++++")
opc = mostrarMenu2("Tercer Menu de opciones", "Alta", "Baja", "Modificacion", "Listar Resultados", "Exportar")
print("Opcion elegida 3:", opc)


print("+++++++++++++++++++++")
opc = mostrarMenu2("Cuarto Menu de opciones")
print("Opcion elegida 4:", opc)
