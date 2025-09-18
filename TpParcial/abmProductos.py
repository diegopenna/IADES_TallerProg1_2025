import libInputs

listaProductos = [
    {'codigo': '00001', 'descripcion': 'Samsung a22', 'categoria': 'Celular', 'precio': 500000.0, 'stock': 30}, 
    {'codigo': '00002', 'descripcion': 'Motorola g10', 'categoria': 'Calular', 'precio': 800000.0, 'stock': 20}
]

def altaProducto():
    producto = {}
    codigo = libInputs.inputAnchoFijo("Ingrese codigo:", 5)
    descripcion = input("Ingrese descripcion:")
    categoria = input("Ingrese categoria:")
    precio = float(input("Ingrese precio:"))
    stock = int(input("Ingrese stock:"))

    producto["codigo"] = codigo
    producto["descripcion"] = descripcion
    producto["categoria"] = categoria
    producto["precio"] = precio
    producto["stock"] = stock

    listaProductos.append(producto)

def mostrarLista():
    for prod in listaProductos:
        print(prod)

menuAbm = {'1':'Alta', '2':'Baja', '3':'Modificación', '4':'Listar', '0':'Salir' }
while True:
    opc = libInputs.mostrarMenu(menuAbm, "****** ABM Productos ******")
    if opc == '0':
        break
    elif opc == '1':
        altaProducto()
    elif opc == '2':
        print("baja")
    elif opc == '3':
        print("Modif")
    elif opc == '4':
        opc2 = libInputs.mostrarMenu({"1":"Codigo", "2":"Descripcion", "3":"Precio", "0":"Cancelar"}, "Ordenar por:")
        if opc2 == "1":
            print("Listado por Codigo")
            mostrarLista()
        elif opc2 == "2":
            print("Listado por Descrip")
        elif opc2 == "3":
            print("Listado por Precio")
    
    
