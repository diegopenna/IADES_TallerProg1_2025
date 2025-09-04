
def mostrarListaPrecios(listaProd):
    print("Lista de Percios")
    print(f"{'Nombre':10}|{"Precio" :8}|{'Cant.':5}|{'total':8}")
    for prod in listaProd:
        print(f"{prod[0] :10}|{prod[1] :8.2f}|{prod[2] :5.2f}|{prod[1] * prod[2] :8.2f}")

def agregarProducto(listaProd, nombre, precio, cantidad):
    producto = [nombre, precio, cantidad]
    listaProd.append(producto)

def borrarProducto(listaProd, indice):
    listaProd.pop(indice)

def modificarProducto(listaProd, indice, nombre, precio, cantidad):
    
    listaProd[indice][0] = nombre
    listaProd[indice][1] = precio
    listaProd[indice][2] = cantidad

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
        print("Codigo Alta")
    elif (opc == 2):
        print("Codigo baja")
    elif (opc == 3):
        print("Codigo modificar")
    elif (opc == 4):
        mostrarListaPrecios(listaProductos)
    if (opc == 5):
        break
