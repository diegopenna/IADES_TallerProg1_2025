from pedidos import Pedido, ItemDePedido
from abmProductos import Producto
import libInputs, abmProductos, pedidos

while True:
    opc = libInputs.mostrarMenu({"1" : "Modulo Productos", "2" : "Modulo Pedidos", "0": "Salir"}, "********SISTEMA DE CONTROL DE STOCK******")
    if opc == "1":
        abmProductos.menuAbmProductos()
    elif opc == "2":
        pedidos.menuPedidos()
    else:
        break

print("Gracias por usar el sistema de Control de Stock")