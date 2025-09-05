
def mostrarListaPrecios(listaProd):
    print("Lista de Percios")
    print(f"{'Nombre':10}|{"Precio" :8}|{'Cant.':5}|{'total':8}")
    print("-" * 34)
    for prod in listaProd:
        print(f"{prod[0] :10}|{prod[1] :8.2f}|{prod[2] :5.2f}|{prod[1] * prod[2] :8.2f}")

    input("Presione enter para continuar....")

def agregarProducto(listaProd):
    print("Alta")
    nombre = input("Ingrese Nombre: ")
    
    if existeNombre(listaProd, nombre):
        print("Ya existe un producto con ese nombre")
    else:
        precio = float(input("Ingrese Precio: "))
        cantidad = float(input("Ingrese Cantidad: "))
        producto = [nombre, precio, cantidad]
        listaProd.append(producto)

def borrarProducto(listaProd):
    print("Borrar")
    nombre = input("Ingrese Nombre: ")

    for i in range(len(listaProd)):
        prod = listaProd[i]
        if prod[0].lower() ==  nombre.lower():
            listaProd.pop(i)
            print("Se elimino el producto", nombre)
            break
    else:
        print("Producto Inexistente")

def modificarProducto(listaProd):
    print("Modificar")
    nombre = input("Ingrese Nombre: ")

    for prod in listaProd:
        if prod[0].lower() ==  nombre.lower():
            nombre = input("Ingrese Nuevo Nombre: ")
            if nombre.lower() != prod[0].lower() and existeNombre(listaProd, nombre):
                print("Ya existe un producto con ese nombre")
            else:
                precio = float(input("Ingrese Precio: "))
                cantidad = float(input("Ingrese Cantidad: "))

                prod[0] = nombre
                prod[1] = precio
                prod[2] = cantidad

                print("Producto", nombre, "mosdificado con exito.")
            break
    else:
        print("Producto Inexistente")

def existeNombre(listaProd, nombre):
    for prod in listaProd:
        if prod[0].lower() == nombre.lower():
            return True
    return False    

def menuDeOpciones():
    print("ABM Productos")
    print("1) Alta")
    print("2) Baja")
    print("3) Modificar")
    print("4) Listar")
    print("5) Salir")
    while True:
        opc = input("Ingrese una Opcion...")
        if (opc in ['1', '2', '3', '4', '5']):
            break
        else:
            print("Opcion Incorrecta.")
    
    return int(opc)

listaProductos = [
    ['Pera', 1000, 2],
    ['Manzana', 1200, 1.5],
    ['Banana', 900, 1], 
    ['Mandarina', 1100, 1]
    ]

while True:
    opc = menuDeOpciones()
    if (opc == 1):
        agregarProducto(listaProductos)
    elif (opc == 2):
        borrarProducto(listaProductos)
    elif (opc == 3):
        modificarProducto(listaProductos)
    elif (opc == 4):
        mostrarListaPrecios(listaProductos)
    if (opc == 5):
        break
