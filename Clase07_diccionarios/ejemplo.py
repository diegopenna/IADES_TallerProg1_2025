
producto = {"codigo": "00001", 
            "descripcion": "Motorola g5", 
            "categoria": "Celular", 
            "precio" : 800000,
            "stock": 100,
            }

print("Descripcion:", producto["descripcion"])
print("Categoria:", producto["categoria"])
print("Precio:",producto["precio"])
print("Codigo:",producto.get("codigo"))
print("Pais:",producto.get("pais"))
print("Pais:",producto.get("pais", "No tiene"))

if ("pais" in producto):
    print(producto["pais"])
else:
    print("El producto no tiene pais de origen")

print(producto.keys())
print(producto.values())
print(producto.items())

print("\nClaves del Producto")
for clave in producto.keys():
    print(clave)


producto["pais"] = "Taiwan"

print("\nDescripion del Producto ahora")
for clave in producto.keys():
    print(clave.title() , ": " ,  producto[clave], sep="")


print("\nDescripion del Producto por item")
for clave, valor in producto.items():
    print(clave.title(), ": " , valor, sep="")


