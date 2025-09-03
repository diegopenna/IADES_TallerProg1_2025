def mostrarListaPrecios(listaProd):
    print("Lista de Percios")
    print(f"{'Nombre':10}|{"Precio" :8}|{'Cant.':5}|{'total':8}")
    for prod in listaProd:
        print(f"{prod[0] :10}|{prod[1] :8.2f}|{prod[2] :5.2f}|{prod[1] * prod[2] :8.2f}")

def agregarProducto(listaProd, nombre, precio, cantidad):
    
    producto = [nombre, precio, cantidad]
    listaProd.append(producto)

def agregarProducto2(listaProd, producto):
    for prod in listaProd:
        if prod[0] == producto[0]:
            return False
    
    listaProd.append(producto)
    return True

def borrarProductolista(listaProd, indice):
    listaProd.pop(indice)

def modificarProducto(listaProd, indice, nombre, precio, cantidad):
    
    listaProd[indice][0] = nombre
    listaProd[indice][1] = precio
    listaProd[indice][2] = cantidad
          



listaProductos = [
    ['Pera', 1000, 2],
    ['Manzana', 1200, 1.5],
    ['Banana', 900, 1], 
    ['Mandarina', 1100, 1]
    ]

mostrarListaPrecios(listaProductos)

agregarProducto(listaProductos, 'Naranja', 2000, 1.5)

mostrarListaPrecios(listaProductos)

agregarProducto2(listaProductos, ["Kiwi", 3800, .5])

mostrarListaPrecios(listaProductos)

if (agregarProducto2(listaProductos, ["Banana", 800, .5])):
    print("Producto Agregado")
else:
    print("Ya existe el producto")

mostrarListaPrecios(listaProductos)

borrarProductolista(listaProductos, 1)

mostrarListaPrecios(listaProductos)

modificarProducto(listaProductos, 1, "Mandarina", 2000, 4)

mostrarListaPrecios(listaProductos)

