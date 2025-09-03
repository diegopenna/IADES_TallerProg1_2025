listaProductos = [
    ['Pera', 1000, 2],
    ['Manzana', 1200, 1.5],
    ['Banana', 900, 1], 
    ['Mandarina', 1100, 1]
    ]


for i in range(len(listaProductos)):
    #print(listaProductos[i])
    for j in range(len(listaProductos[i])):
        print(f"{listaProductos[i][j] :10}", end="|")
    print("")

print("")
for i in range(len(listaProductos)):
    #print(listaProductos[i])
    for j in range(len(listaProductos[i])):
        print(i, j , end="|")
    print("")
