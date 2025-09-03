#listaProduc = ['Pera', 'Manzana', 'Banana' , 'Mandarina']
#listaPrecios = [1000, 1200, 900, 1100]
#listaCantiad = [2, 1.5, 1, 1]

listaProductos = [
    ['Pera', 1000, 2],
    ['Manzana', 1200, 1.5],
    ['Banana', 900, 1], 
    ['Mandarina', 1100, 1]
    ]

print(len(listaProductos))

#Producto Manzana
print(listaProductos[1])
print(listaProductos[1][2])

unproducto = listaProductos[2]

print(unproducto)
print("Nombre", unproducto[0])
print("Precio", unproducto[1])
print("Cantidad", unproducto[2])


for i in range(len(listaProductos)):
    #print(listaProductos[i])
    for j in range(len(listaProductos[i])):
        print(i, j, "-", listaProductos[i][j])

