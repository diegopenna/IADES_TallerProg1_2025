import libInputs, pathlib, pickle, abmProductos

class Pedido:
    def __init__(self):
        self.nroPedido = 0
        self.cuit = ""
        self.nombre = ""
        self.items = []
    
    def mostrar(self):
        print("Pedido Nro.", self.nroPedido)
        print("CUIT:", self.cuit, " Nombre:", self.nombre)
        for unItem in self.items:
            print(str(unItem))
        print(f"                                           Cantidad de items: {self.cantidadItems() :11d}" )
        print(f"                                                 Monto Total: {self.importeTotal() :11.2f}" )

    def cantidadItems(self):
        return len(self.items)
    
    def importeTotal(self):
        total = 0.0
        for unItem in self.items:
            unItem : ItemDePedido
            total = total + unItem.importe()
        #El round es para eliminar el error que se produce por sumas de numeros con punto flotante
        return round(total, 2)

class ItemDePedido:
    def __init__(self):
        self.orden = 0
        self.codigoProd = ""
        self.descripcionProd = ""
        self.precioProd = 0.0
        self.cantidad = 0
    
    def __str__(self):
        return f"#{self.orden :5d} {self.descripcionProd[:20] :20}  Precio: {self.precioProd :10.2f} x { self.cantidad :2d} Importe: {self.importe() :11.2f}"

    def importe(self):
        return self.cantidad * self.precioProd

nombreArchivo = "listaPedidos.lst"
listaPedidos = []

def menuPedidos():
    while True:
        opc = libInputs.mostrarMenu({"1": "Alta pedido", "2" : "Ver Pedido", "3":"Listar Pedidos", "0" : "Volver al menu anterior"}, "****** PEDIDOS ******")
        if opc == "1":
            altaPedido()
        elif opc == "2":
            verPedido()
        elif opc == "3":
            listarPedidos()
        else:
            break

def altaPedido():
    nombre = libInputs.inputAnchoMaximoObligatorio("Ingrese Nombre: ", 200)
    cuit = libInputs.inputAnchoFijo("Ingrese Cuit: ", 11,soloNumeros=True)
    items = []
    while True:
        codigo = libInputs.inputAlfanuNumerico("Ingrese Codigo: ",anchofijo=5)
        prod = abmProductos.buscarPorCodigo(codigo)

        if prod == None:
            print("Error: Producto Inexistente")
            continue
        print()
        prod.mostrar()
        
        #Control que no exista producto en pedido
        existeEnPedido = False
        for itm in items:
            itm : ItemDePedido
            if (itm.codigoProd == prod.codigo):
                print("Error: El producto ya se encuentra cargado en el pedido.")
                existeEnPedido = True
                break
        
        if existeEnPedido:
            continue
        #Fin control que no exista producto en pedido

        opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "Continuar con el producto seleccionado? ")
        
        if opc == "n":
            continue

        
        cantidad = libInputs.inputInt("Ingrese cantidad",validaPositivo=True, permiteCero=False)
        if prod.stock >= cantidad:
            unItemDePedido = ItemDePedido()
            unItemDePedido.codigoProd = prod.codigo
            unItemDePedido.descripcionProd = prod.descripcion
            unItemDePedido.precioProd = prod.precio
            unItemDePedido.cantidad = cantidad
            unItemDePedido.orden = len(items) + 1
            items.append(unItemDePedido)
        else: 
            print("Error: No hay stock disponible para el producto seleccionado")

        opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "Desea cargar otro item? ")
        if opc == "n":
            break
    
    unPedido = Pedido()
    unPedido.nombre = nombre
    unPedido.cuit = cuit
    unPedido.items = items
    unPedido.nroPedido = len(listaPedidos) + 1 

    print("Se va a dar de alta el siguiente pedido:")
    unPedido.mostrar()
    opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "Desea confirmar? ")

    if opc == 's':
        listaPedidos.append(unPedido)
        for itm in unPedido.items:
            prod = abmProductos.buscarPorCodigo(itm.codigoProd)
            prod.stock = prod.stock - itm.cantidad
        
        abmProductos.guardarListaProductos()
        guardarListaPedidos()    


    print("\nSe dio de alta el siguiente pedido:")
    unPedido.mostrar()
    input("\nPresione Enter para continuar...")


def verPedido():
    nroPedido = libInputs.inputInt("Ingrese Nro. Pedido:",validaPositivo=True, permiteCero=False)
    if nroPedido > len(listaPedidos):
        print("Error: Pedido Inexistente.")
        input("\nPresione Enter para continuar...")
        return False

    unPedido = listaPedidos[nroPedido -1]
    unPedido.mostrar()
    input("\nPresione Enter para continuar...")

def listarPedidos():
    for unPedido in listaPedidos:
        unPedido : Pedido
        print(f"{unPedido.nroPedido :5d} | {unPedido.cuit :11} | {unPedido.nombre[:20] :20} | {unPedido.cantidadItems() :5d} | {unPedido.importeTotal() :11.2f}")

    opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "Desea Exportar Listado? ")
    if opc == "s":
        exportarlistado()
    input("\nPresione Enter para continuar...")

def exportarlistado():
    while True:
        nombreArchivo = libInputs.inputAnchoMaximoObligatorio("Ingrese Nombre de archivo", 255)
        arch = pathlib.Path(nombreArchivo)
        if arch.exists():
            opc = libInputs.mostrarMenu({"s": "Si", "n":"No"}, "El archivo existe. Desea sobreescibirlo?")
            if (opc == "n"):
                continue  
        try:              
            with open(nombreArchivo, 'w', encoding="utf8") as f:
                for unPedido in listaPedidos:
                    unPedido : Pedido
                    #f.write(f"{unPedido.nroPedido :5d} | {unPedido.cuit :11} | {unPedido.nombre[:20] :20} | {unPedido.cantidadItems() :5d} | {unPedido.importeTotal() :11.2f}\n")
                    print(f"{unPedido.nroPedido :5d} | {unPedido.cuit :11} | {unPedido.nombre[:20] :20} | {unPedido.cantidadItems() :5d} | {unPedido.importeTotal() :11.2f}", file=f)
            print("El listado se exporto en: ", nombreArchivo)
        except Exception as err:
            print("Ocurrio un error al intentar exportar el archivo. Error: ", err)
        else:
            break

def cargarListaPedidos():
    global listaPedidos
    arch = pathlib.Path(nombreArchivo)
    if (arch.exists()):
        with open(nombreArchivo, 'rb') as f:
            listaPedidos = pickle.load(f)
    


def guardarListaPedidos():
    with open(nombreArchivo, 'wb') as f:
        pickle.dump(listaPedidos, f)



cargarListaPedidos()

if (__name__ == '__main__'):
    menuPedidos()