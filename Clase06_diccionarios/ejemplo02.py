listaProductos = [
    {'nombre':'Pera', 'origen':'Brasil' , 'precio':1000, 'peso':2 },
    {'nombre':'Manzana', 'precio':1200, 'peso':1.5},
    {'nombre':'Banana', 'precio':900, 'peso':1}, 
    {'nombre':'Mandarina', 'precio':1100, 'peso':1}
    ]

pera = listaProductos[0]
print("Recorro claves")
for clave in pera.keys():
    print(clave)

print("Recorro valores")
for valor in pera.values():
    print(valor)

print("\nRrecorro Lista y Propiedades, por clave\n")
for prod in listaProductos:
    for clave in prod: # es lo mismo pord.keys()
        print(f"{clave}: {prod[clave]}")
        #print(clave, prod[clave])


print("\nRrecorro Lista y Propiedades, por item\n")
for prod in listaProductos:
    for clave, valor in prod.items():
        print(f"{clave}: {valor}")
        #print(clave, valor)
