import libInputs, pathlib, pickle, abmProductos

class Pedido:
    def __init__(self):
        self.nroPedido = 0
        self.cuit = ""
        self.nombre = ""
        self.items = []

class ItemDePedido:
    def __init__(self):
        self.orden = 0
        self.codigoProd = ""
        self.descripcionProd = ""
        self.precioProd = 0.0
        self.cantidad = 0

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
            listarPedido()
        else:
            break

def altaPedido():
    #TODO: Desarrollar alta pedidos
    nombre = input("Ingrese Nombre")
    cuit = input("Ingrse Cuit")
    items = []
    while True:
        codigo = input("Ingrese Codigo")
        prod = abmProductos.buscarPorCodigo(codigo)
        #Validar que exista el producto
        #Validar que el producto no este en el pedido
        if prod != None:
            cantidad = int(input("Ingrese cantidad"))
            #Validar cantidad contea stock
            unItemDePedido = ItemDePedido()
            unItemDePedido.codigoProd = prod.codigo
            unItemDePedido.descripcionProd = prod.descripcion
            unItemDePedido.precioProd = prod.precio
            unItemDePedido.cantidad = cantidad
            unItemDePedido.orden = len(items) + 1
            items.append(unItemDePedido)
        
        opc = input("Otro Item? s/n")
        if opc == "n":
            break
    
    unPedido = Pedido()
    unPedido.nombre = nombre
    unPedido.cuit = cuit
    unPedido.items = items
    unPedido.nroPedido = len(listaPedidos) + 1 
    listaPedidos.append(unPedido)
    #Falta descontar stock de productos
    guardarListaPedidos()
     
        
    print("Desarrollar alta pedidos")

def verPedido():
    #TODO: Desarrollar Ver pedido
    print("Desarrollar ver pedido")   

def listarPedido():
    #TODO: Desarrollar listar pedidos
    print("Desarrollar listar pedidos")


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
menuPedidos()