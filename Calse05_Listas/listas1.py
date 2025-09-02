def mostrarListaPrecios(listaProd, listaPrec, listaCant):
    print("Lista de Percios")
    for i in range(len(listaProd)):
        print(listaProd[i], listaPrec[i], listaCant[i])

listaProductos = ['Pera', 'Manzana', 'Banana' , 'Mandarina']
listaPrecios = [1000, 1200, 900, 1100]
listaCantiad = [2, 1.5, 1, 1]

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)

listaProductos.append('Naranja')
listaPrecios.append(2000)
listaCantiad.append(1.5)

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)

listaProductos.append('Uva')
listaPrecios.append(4000)

mostrarListaPrecios(listaProductos, listaPrecios, listaCantiad)
