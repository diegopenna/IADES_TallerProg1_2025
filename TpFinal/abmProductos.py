import libInputs

class Producto:
    def __init__(self, codigo = "", descripcion = "", categoria = "", precio = 0.0, stock = 0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        

listaProductos = [
    Producto('00001', 'Samsung A22', 'Celular', 500000.0, 30),
    Producto('00002', 'Motorola G10', 'Celular', 800000.0, 20),
    Producto('00003', 'iPhone 13', 'Celular', 1500000.0, 15),
    Producto('00004', 'Xiaomi Redmi Note 11', 'Celular', 600000.0, 25),
    Producto('00005', 'Notebook Lenovo IdeaPad 3', 'Notebook', 1200000.0, 12),
    Producto('00006', 'Notebook HP Pavilion 15', 'Notebook', 1350000.0, 10),
    Producto('00007', 'Notebook Dell Inspiron 14', 'Notebook', 1400000.0, 8),
    Producto('00008', 'Notebook Asus VivoBook', 'Notebook', 1250000.0, 9),
    Producto('00009', 'Tablet Samsung Galaxy Tab A7', 'Tablet', 700000.0, 18),
    Producto('00010', 'iPad 9na Generación', 'Tablet', 1100000.0, 14),
    Producto('00011', 'Tablet Lenovo Tab M10', 'Tablet', 650000.0, 20),
    Producto('00012', 'Tablet Huawei MatePad T10', 'Tablet', 680000.0, 16),
    Producto('00013', 'Mouse Logitech M170', 'Periférico', 15000.0, 100),
    Producto('00014', 'Teclado Redragon Kumara', 'Periférico', 45000.0, 50),
    Producto('00015', 'Monitor Samsung 24"', 'Periférico', 180000.0, 20),
    Producto('00016', 'Impresora HP DeskJet 2710', 'Periférico', 120000.0, 15),
    Producto('00017', 'Disco Rígido WD Blue 1TB', 'Almacenamiento', 90000.0, 30),
    Producto('00018', 'SSD Kingston A400 480GB', 'Almacenamiento', 85000.0, 25),
    Producto('00019', 'Pendrive Sandisk 64GB', 'Almacenamiento', 20000.0, 60),
    Producto('00020', 'Tarjeta MicroSD Samsung 128GB', 'Almacenamiento', 35000.0, 40),
    Producto('00021', 'Funda iPhone 13 Transparente', 'Funda', 5000.0, 70),
    Producto('00022', 'Funda Samsung A22 Negra', 'Funda', 4500.0, 60),
    Producto('00023', 'Funda Universal Tablet 10"', 'Funda', 8000.0, 40),
    Producto('00024', 'Funda Notebook 15.6"', 'Funda', 15000.0, 30),
    Producto('00025', 'Cargador Samsung 25W', 'Cargador', 20000.0, 50),
    Producto('00026', 'Cargador Motorola TurboPower', 'Cargador', 22000.0, 45),
    Producto('00027', 'Cargador Apple 20W USB-C', 'Cargador', 35000.0, 35),
    Producto('00028', 'Cable USB-C a USB 1m', 'Cable', 5000.0, 80),
    Producto('00029', 'Cable HDMI 2m', 'Cable', 7000.0, 70),
    Producto('00030', 'Auriculares Inalámbricos JBL', 'Auricular', 60000.0, 40)
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
    #producto = {}
    producto = Producto()
    while True:
        codigo = libInputs.inputAlfanuNumerico("Ingrese codigo:", 5)
        if buscarPorCodigo(codigo) == None:
            break
        else:
            print("Error: El codigo ingresado ya existe")
    descripcion = libInputs.inputAnchoMaximo("Ingrese descripcion:", 200)
    categoria = libInputs.inputOpciones("Ingrese categoria:", listaCategorias)
    precio = libInputs.inputFloat("Ingrese precio:", validaPositivo=True, permiteCero=False)
    stock =  libInputs.inputInt("Ingrese stock:", validaPositivo=True, permiteCero=True)
    
    #producto["codigo"] = codigo
    producto.codigo = codigo
    producto.descripcion = descripcion
    producto.categoria = categoria
    producto.precio = precio
    producto.stock = stock

    listaProductos.append(producto)

def bajaProducto():
    print("\nBaja de Producto")
    codigo = libInputs.inputAlfanuNumerico("Ingrese codigo a dar de baja:", 5)
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
    codigo = libInputs.inputAlfanuNumerico("Ingrese codigo a modificar:", 5)
    prod:Producto = buscarPorCodigo(codigo)
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
                codigo = libInputs.inputAlfanuNumerico("Ingrese codigo:", 5)
                if prod.codigo != codigo:
                    if buscarPorCodigo(codigo) == None:
                        break
                    else:
                        print("Error: El codigo ingresado ya existe")
                prod.codigo = codigo
        elif opc == "2":
            descripcion = libInputs.inputAnchoMaximo("Ingrese descripcion:", 200)
            prod.descripcion = descripcion
        elif opc == "3":
            categoria = libInputs.inputOpciones("Ingrese categoria:", listaCategorias)
            prod.categoria = categoria
        elif opc == "4":
            precio = libInputs.inputFloat("Ingrese precio:", validaPositivo=True, permiteCero=False)
            prod.precio = precio
        elif opc == "5":
            stock =  libInputs.inputInt("Ingrese stock:", validaPositivo=True, permiteCero=True)
            prod.stock = stock
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
            prod1:Producto = lista[i]
            prod2:Producto = lista[i + 1]
            valor1 = prod1.__getattribute__(orden)
            valor2 = prod2.__getattribute__(orden) 
            if (valor1 > valor2):
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
        print(f"{prod.codigo :6}|{prod.descripcion :30}|{prod.categoria:15}|{prod.precio:16.2f}|{prod.stock:6d}")

def buscarPorCodigo(codigo):
    for prod in listaProductos:
        if (prod.codigo == codigo):
            return prod

def mostrarProducto(producto:Producto):
    print("Descripción del Producto")
    print("     Codigo:", producto.codigo)
    print("Descripcion:", producto.descripcion)
    print("  Categoría:", producto.categoria)
    print("     Precio:", producto.precio)
    print("      Stock:", producto.stock)

menuAbmProductos()


    
    
