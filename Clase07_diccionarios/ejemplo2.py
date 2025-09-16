
def mostrarProducto(producto, titulo = "Descripción Producto:"):
    print(f"\n{titulo}")
    for clave, valor in producto.items():
        print(clave.title(), ": " , valor, sep="")

producto1 = {"codigo": "00001", 
            "descripcion": "Motorola g5", 
            "categoria": "Celular", 
            "precio" : 800000,
            "stock": 100,
            }

producto2 = producto1

mostrarProducto(producto1, "Producto 1")
mostrarProducto(producto2, "Producto 2")

print("\nModifico Producto 2")
producto2["codigo"] = "00002"

mostrarProducto(producto1, "Producto 1")
mostrarProducto(producto2, "Producto 2")

producto2 = dict(producto1)

print("\nModifico Producto 2")
producto2["codigo"] = "00003"

mostrarProducto(producto1, "Producto 1")
mostrarProducto(producto2, "Producto 2")
