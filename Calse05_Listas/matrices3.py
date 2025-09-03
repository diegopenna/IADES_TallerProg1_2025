listaProductos = [
    ['Pera', 1000, 2],
    ['Manzana', 1200, 1.5],
    ['Banana', 900, 1], 
    ['Mandarina', 1100, 1]
    ]

print(f"{'Nombre':10}|{"Precio" :8}|{'Cant.':5}|{'total':8}")
for prod in listaProductos:
    #print(prod)
    #print(prod[0], prod[1], prod[2], prod[1] * prod[2])
    print(f"{prod[0] :10}|{prod[1] :8.2f}|{prod[2] :5.2f}|{prod[1] * prod[2] :8.2f}")
