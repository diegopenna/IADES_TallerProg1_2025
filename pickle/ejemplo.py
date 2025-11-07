import pathlib, pickle

listaProductos = []

rutaLista = ".\pickle\listaProductos.lst"

def cargarLista():
    global listaProductos
    arch = pathlib.Path(rutaLista)
    if arch.exists():
        with open(rutaLista, "rb") as f:
            listaProductos = pickle.load(f)
    else:
        listaProductos = []

def guardarLista():
    with open(rutaLista, "wb") as f:
        pickle.dump(listaProductos, f)


cargarLista()
prod = {'codigo': '00031', 'descripcion': 'Otra Descrcipcin', 'categoria': 'Celular', 'precio': 10000.0, 'stock': 10}
listaProductos.append(prod)

guardarLista()
print(listaProductos)