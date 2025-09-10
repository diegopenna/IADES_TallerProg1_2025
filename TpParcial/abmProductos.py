
listaProductos = [
    {'codigo': '0001', 'descripcion': 'Samsung a22', 'categoria': 'Celular', 'precio': 500000.0, 'stock': 30}, 
    {'codigo': '0002', 'descripcion': 'Motorola g10', 'categoria': 'Calular', 'precio': 800000.0, 'stock': 20}
]

def altaProducto(lista):
    producto = {}
    codigo = input("Ingrese codigo:")
    descripcion = input("Ingrese descripcion:")
    categoria = input("Ingrese categoria:")
    precio = float(input("Ingrese precio:"))
    stock = int(input("Ingrese stock:"))

    producto["codigo"] = codigo
    producto["descripcion"] = descripcion
    producto["categoria"] = categoria
    producto["precio"] = precio
    producto["stock"] = stock

    lista.append(producto)

def mostrarLista(lista):
    for prod in lista:
        print(prod)

altaProducto(listaProductos)
mostrarLista(listaProductos)
