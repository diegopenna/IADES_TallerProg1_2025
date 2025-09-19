import libInputs

listaProductos = [
    {'codigo': '00001', 'descripcion': 'Samsung a22', 'categoria': 'Celular', 'precio': 500000.0, 'stock': 30}, 
    {'codigo': '00002', 'descripcion': 'Motorola g10', 'categoria': 'Calular', 'precio': 800000.0, 'stock': 20}
]

listaCategorias = ["Notebook", "Celular", "Tablet", "Periférico", "Almacenamiento", "Funda", "Cargador", "Cable", "Auricular"]

def menuAbmProductos():
    menuAbm = {'1':'Alta', 
            '2':'Baja', 
            '3':'Modificación', 
            '4':'Listar', 
            '0':'Salir' }
    while True:
        opc = libInputs.mostrarMenu(menuAbm, "****** ABM Productos ******")
        if opc == '0':
            break
        elif opc == '1':
            altaProducto()
        elif opc == '2':
            bajaProducto()
        elif opc == '3':
            modificarProducto()
        elif opc == '4':
            opc2 = libInputs.mostrarMenu({"1":"Codigo", "2":"Descripcion", "3":"Precio", "0":"Cancelar"}, "Ordenar por:")
            if opc2 == "1":
                print("Listado por Codigo")
                listarProductos()
            elif opc2 == "2":
                print("Listado por Descrip")
            elif opc2 == "3":
                print("Listado por Precio")

def altaProducto():
    producto = {}
    codigo = libInputs.inputAnchoFijo("Ingrese codigo:", 5)
    descripcion = libInputs.inputAnchoMaximo("Ingrese descripcion:", 200)
    categoria = libInputs.inputOpciones("Ingrese categoria:", listaCategorias)
    precio = libInputs.inputFloat("Ingrese precio:", validaPositivo=True, permiteCero=False)
    stock =  libInputs.inputInt("Ingrese stock:", validaPositivo=True, permiteCero=True)

    producto["codigo"] = codigo
    producto["descripcion"] = descripcion
    producto["categoria"] = categoria
    producto["precio"] = precio
    producto["stock"] = stock

    listaProductos.append(producto)

def bajaProducto():
    print("Aca va el codigo de la baja")

def modificarProducto():
    print("Aca va el codigo de la modificacion")

def listarProductos():
    for prod in listaProductos:
        print(prod)

menuAbmProductos()

    
    
