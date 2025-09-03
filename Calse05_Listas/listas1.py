def mostrarListaPrecios(listaProd, listaPrec, listaCant):
    print("Lista de Percios")
    for i in range(len(listaProd)):
        print(listaProd[i], listaPrec[i], listaCant[i])

def agregarProducto(listaProd, listaPrec, listaCant, nombre, precio, cantidad):
    listaProd.append(nombre)
    listaPrec.append(precio)
    listaCant.append(cantidad)

def borrarProductolista(listaProd, listaPrec, listaCant, indice):
    listaProd.pop(indice)
    listaPrec.pop(indice)
    listaCant.pop(indice)

def modificarProducto(listaProd, listaPrec, listaCant, indice, nombre, precio, cantidad):
    listaProd[indice] = nombre
    listaPrec[indice] = precio
    listaCant[indice] = cantidad
    print("Modificar Producto")


listaProductos = ['Pera', 'Manzana', 'Banana' , 'Mandarina']
listaPrecios = [1000, 1200, 900, 1100]
listaCantiad = [2, 1.5, 1, 1]

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)

agregarProducto(listaProductos, listaPrecios, listaCantiad, 'Naranja', 2000, 1.5)

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)

borrarProductolista(listaProductos, listaPrecios, listaCantiad, 1)

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)

modificarProducto(listaProductos, listaPrecios, listaCantiad, 2,  "Sandia", 2200, 3)

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)

