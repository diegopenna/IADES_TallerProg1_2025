listaProductos = [
    {'nombre':'Pera', 'precio':1000, 'peso':2 , 'origen':'Brasil'},
    {'nombre':'Manzana', 'precio':1200, 'peso':1.5},
    {'nombre':'Banana', 'precio':900, 'peso':1}, 
    {'nombre':'Mandarina', 'precio':1100, 'peso':1}
    ]

for prod in listaProductos:
    print('Nom:', prod['nombre'])
    print('Prec:',prod['precio'])
    print('Peso:',prod['peso'])
    if ('origen' in prod):
        print('Orig:',prod['origen'])

prod = listaProductos[0]
print(prod)
print(prod['origen'])

prod = listaProductos[1]
print(prod)
print(prod.get('origen'))
#print(prod['origen'])

pera = listaProductos[0]

print("Pera")
print("Len", len(pera))
