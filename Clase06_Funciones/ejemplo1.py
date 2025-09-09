def descripcionUsuario(pApellido, pNombre, pSegNombre = None, pDni = None ):
    if (pSegNombre == None): 
        pSegNombre = ""
    else:
        pSegNombre = " " + pSegNombre    
    if (pDni == None): 
        pDni = "--Sin DNI--"
    return f"{pApellido}, {pNombre}{pSegNombre} - Dni: {pDni}" 

lista = [
    ["Penna", "Diego", "Fernando", "26620884"],
    ["Perez", "Valentina", None, None],
    ["Marelli", "Agustin", "Ezequiel", None]
]

for i in range(len(lista)):
    print(f"\nUsuario {i}\n")
    apellido = lista[i][0]
    nombre = lista[i][1]
    segNombre = lista[i][2]
    dni = lista[i][3]

    print(descripcionUsuario(apellido, nombre))
    print(descripcionUsuario(pNombre=nombre, pApellido=apellido))
    print(descripcionUsuario(apellido, nombre, segNombre))
    print(descripcionUsuario(apellido, nombre, segNombre, dni))
    print(descripcionUsuario(apellido, nombre, pDni=dni))
    #da error porque falta el parametro pNombre:
    # print(descripcionUsuario(apellido, pDni=dni))


