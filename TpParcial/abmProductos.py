import libInputs

listaProductos = [
    {'codigo': '00001', 'descripcion': 'Samsung A22', 'categoria': 'Celular', 'precio': 500000.0, 'stock': 30},
    {'codigo': '00002', 'descripcion': 'Motorola G10', 'categoria': 'Celular', 'precio': 800000.0, 'stock': 20},
    {'codigo': '00003', 'descripcion': 'iPhone 13', 'categoria': 'Celular', 'precio': 1500000.0, 'stock': 15},
    {'codigo': '00004', 'descripcion': 'Xiaomi Redmi Note 11', 'categoria': 'Celular', 'precio': 600000.0, 'stock': 25},
    {'codigo': '00005', 'descripcion': 'Notebook Lenovo IdeaPad 3', 'categoria': 'Notebook', 'precio': 1200000.0, 'stock': 12},
    {'codigo': '00006', 'descripcion': 'Notebook HP Pavilion 15', 'categoria': 'Notebook', 'precio': 1350000.0, 'stock': 10},
    {'codigo': '00007', 'descripcion': 'Notebook Dell Inspiron 14', 'categoria': 'Notebook', 'precio': 1400000.0, 'stock': 8},
    {'codigo': '00008', 'descripcion': 'Notebook Asus VivoBook', 'categoria': 'Notebook', 'precio': 1250000.0, 'stock': 9},
    {'codigo': '00009', 'descripcion': 'Tablet Samsung Galaxy Tab A7', 'categoria': 'Tablet', 'precio': 700000.0, 'stock': 18},
    {'codigo': '00010', 'descripcion': 'iPad 9na Generación', 'categoria': 'Tablet', 'precio': 1100000.0, 'stock': 14},
    {'codigo': '00011', 'descripcion': 'Tablet Lenovo Tab M10', 'categoria': 'Tablet', 'precio': 650000.0, 'stock': 20},
    {'codigo': '00012', 'descripcion': 'Tablet Huawei MatePad T10', 'categoria': 'Tablet', 'precio': 680000.0, 'stock': 16},
    {'codigo': '00013', 'descripcion': 'Mouse Logitech M170', 'categoria': 'Periférico', 'precio': 15000.0, 'stock': 100},
    {'codigo': '00014', 'descripcion': 'Teclado Redragon Kumara', 'categoria': 'Periférico', 'precio': 45000.0, 'stock': 50},
    {'codigo': '00015', 'descripcion': 'Monitor Samsung 24"', 'categoria': 'Periférico', 'precio': 180000.0, 'stock': 20},
    {'codigo': '00016', 'descripcion': 'Impresora HP DeskJet 2710', 'categoria': 'Periférico', 'precio': 120000.0, 'stock': 15},
    {'codigo': '00017', 'descripcion': 'Disco Rígido WD Blue 1TB', 'categoria': 'Almacenamiento', 'precio': 90000.0, 'stock': 30},
    {'codigo': '00018', 'descripcion': 'SSD Kingston A400 480GB', 'categoria': 'Almacenamiento', 'precio': 85000.0, 'stock': 25},
    {'codigo': '00019', 'descripcion': 'Pendrive Sandisk 64GB', 'categoria': 'Almacenamiento', 'precio': 20000.0, 'stock': 60},
    {'codigo': '00020', 'descripcion': 'Tarjeta MicroSD Samsung 128GB', 'categoria': 'Almacenamiento', 'precio': 35000.0, 'stock': 40},
    {'codigo': '00021', 'descripcion': 'Funda iPhone 13 Transparente', 'categoria': 'Funda', 'precio': 5000.0, 'stock': 70},
    {'codigo': '00022', 'descripcion': 'Funda Samsung A22 Negra', 'categoria': 'Funda', 'precio': 4500.0, 'stock': 60},
    {'codigo': '00023', 'descripcion': 'Funda Universal Tablet 10"', 'categoria': 'Funda', 'precio': 8000.0, 'stock': 40},
    {'codigo': '00024', 'descripcion': 'Funda Notebook 15.6"', 'categoria': 'Funda', 'precio': 15000.0, 'stock': 30},
    {'codigo': '00025', 'descripcion': 'Cargador Samsung 25W', 'categoria': 'Cargador', 'precio': 20000.0, 'stock': 50},
    {'codigo': '00026', 'descripcion': 'Cargador Motorola TurboPower', 'categoria': 'Cargador', 'precio': 22000.0, 'stock': 45},
    {'codigo': '00027', 'descripcion': 'Cargador Apple 20W USB-C', 'categoria': 'Cargador', 'precio': 35000.0, 'stock': 35},
    {'codigo': '00028', 'descripcion': 'Cable USB-C a USB 1m', 'categoria': 'Cable', 'precio': 5000.0, 'stock': 80},
    {'codigo': '00029', 'descripcion': 'Cable HDMI 2m', 'categoria': 'Cable', 'precio': 7000.0, 'stock': 70},
    {'codigo': '00030', 'descripcion': 'Auriculares Inalámbricos JBL', 'categoria': 'Auricular', 'precio': 60000.0, 'stock': 40},
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
            menuOrden = {"1":"Código", "2":"Descripción", "3":"Precio", "4":"Categoría", "5":"Stock", "0":"Cancelar"}
            columnas = {"1":"codigo", "2":"descripcion", "3":"precio", "4":"categoria", "5":"stock"}
            opc2 = libInputs.mostrarMenu(menuOrden, "Ordenar por:")
            if opc2 != "0":
                print("Listado por", menuOrden[opc2])
                listaOrdenada = ordenarProductos(columnas[opc2])
                imprimirListaProd(listaOrdenada)
        
        input("Presione Enter para continuar...")


def altaProducto():
    print("\nAlta de Producto")
    producto = {}
    while True:
        codigo = libInputs.inputAnchoFijo("Ingrese codigo:", 5)
        if buscarPorCodigo(codigo) == None:
            break
        else:
            print("Error: El codigo ingresado ya existe")
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
    print("\nBaja de Producto")
    codigo = libInputs.inputAnchoFijo("Ingrese codigo a dar de baja:", 5)
    prod = buscarPorCodigo(codigo)
    if prod == None:
        print("El codigo ingresado es inexistente")
        return
    print("\nProducto Encontrado")
    mostrarProducto(prod)
    opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "Confirma la baja del producto seleccionado?")
    if opc == "s":
        listaProductos.remove(prod)
        print("Producto eliminado con exito")
    else:
        print("Operacion cancelada")
    
    

def modificarProducto():
    print("\nModificar Producto")
    codigo = libInputs.inputAnchoFijo("Ingrese codigo a modificar:", 5)
    prod = buscarPorCodigo(codigo)
    if prod == None:
        print("El codigo ingresado es inexistente")
        return
    
    print("\nProducto Encontrado")
    mostrarProducto(prod)

    #opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "Desea modificar el producto seleccionado?")
    #if opc == "n":
    #    return
    while True:
        opc = libInputs.mostrarMenu({"1": "Codigo", "2": "Descripcion", "3" : "Categoria", "4" : "Precio", "5": "Stock", "0" : "Finalizar Modifciacion"}, "Ingrese el campo que desea modificar")
        if opc == "1":
            while True:
                codigo = libInputs.inputAnchoFijo("Ingrese codigo:", 5)
                if prod["codigo"] != codigo:
                    if buscarPorCodigo(codigo) == None:
                        break
                    else:
                        print("Error: El codigo ingresado ya existe")
                prod["codigo"] = codigo
        elif opc == "2":
            descripcion = libInputs.inputAnchoMaximo("Ingrese descripcion:", 200)
            prod["descripcion"] = descripcion
        elif opc == "3":
            categoria = libInputs.inputOpciones("Ingrese categoria:", listaCategorias)
            prod["categoria"] = categoria
        elif opc == "4":
            precio = libInputs.inputFloat("Ingrese precio:", validaPositivo=True, permiteCero=False)
            prod["precio"] = precio
        elif opc == "5":
            stock =  libInputs.inputInt("Ingrese stock:", validaPositivo=True, permiteCero=True)
            prod["stock"] = stock
        elif opc == "0":
            break

        mostrarProducto(prod)
    
    print("\nProducto modificado con exito")

    
    

def ordenarProductos(orden):
    lista = list(listaProductos)
    intercambio = True
    ultimo = 1
    while intercambio:
        intercambio = False
        for i in range(len(lista) - ultimo):
            if (lista[i][orden] > lista[i + 1][orden]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                intercambio = True
        ultimo += 1

    return lista

def imprimirListaProd(lista):
    #imprime Cabecera
    print(f"{'Código' :6}|{'Descripción' :30}|{'Categoría':15}|{'Precio':16}|{'Stock':6}")
    print(f"{'-' * 6}|{'-' * 30}|{'-' * 15}|{'-' * 16}|{'-' * 6}")
    for prod in lista:
        #imprime Items
        print(f"{prod['codigo'] :6}|{prod['descripcion'] :30}|{prod['categoria']:15}|{prod['precio']:16.2f}|{prod['stock']:6d}")

def buscarPorCodigo(codigo):
    for prod in listaProductos:
        if (prod['codigo'] == codigo):
            return prod

def mostrarProducto(producto):
    print("Descripción del Producto")
    print("     Codigo:", producto["codigo"])
    print("Descripcion:", producto["descripcion"])
    print("  Categoría:", producto["categoria"])
    print("     Precio:", producto["precio"])
    print("      Stock:", producto["stock"])

menuAbmProductos()


    
    
