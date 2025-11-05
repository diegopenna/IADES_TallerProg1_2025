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
    {'codigo': '00017', 'descripcion': 'Disco Rígido "WD Blue 1TB"', 'categoria': 'Almacenamiento', 'precio': 90000.0, 'stock': 30},
    {'codigo': '00018', 'descripcion': 'SSD Kingston A400 480GB', 'categoria': 'Almacenamiento', 'precio': 85000.0, 'stock': 25},
    {'codigo': '00019', 'descripcion': 'Pendrive Sandisk ;64GB', 'categoria': 'Almacenamiento', 'precio': 20000.0, 'stock': 60},
    {'codigo': '00020', 'descripcion': 'Tarjeta "MicroSD" Samsung 128GB', 'categoria': 'Almacenamiento', 'precio': 35000.0, 'stock': 40},
    {'codigo': '00021', 'descripcion': 'Funda iPhone 13 \n Transparente', 'categoria': 'Funda', 'precio': 5000.0, 'stock': 70},
    {'codigo': '00022', 'descripcion': 'Funda Samsung A22 Negra', 'categoria': 'Funda', 'precio': 4500.0, 'stock': 60},
    {'codigo': '00023', 'descripcion': 'Funda Universal Tablet 10"', 'categoria': 'Funda', 'precio': 8000.0, 'stock': 40},
    {'codigo': '00024', 'descripcion': 'Funda Notebook 15.6"', 'categoria': 'Funda', 'precio': 15000.0, 'stock': 30},
    {'codigo': '00025', 'descripcion': 'Cargador Samsung 25W', 'categoria': 'Cargador', 'precio': 20000.0, 'stock': 50},
    {'codigo': '00026', 'descripcion': 'Cargador\nMotorola\nTurboPower', 'categoria': 'Cargador', 'precio': 22000.0, 'stock': 45},
    {'codigo': '00027', 'descripcion': 'Cargador Apple 20W USB-C', 'categoria': 'Cargador', 'precio': 35000.0, 'stock': 35},
    {'codigo': '00028', 'descripcion': 'Cable \t\tUSB-C a USB 1m', 'categoria': 'Cable', 'precio': 5000.0, 'stock': 80},
    {'codigo': '00029', 'descripcion': 'Cable HDMI 2m', 'categoria': 'Cable', 'precio': 7000.0, 'stock': 70},
    {'codigo': '00030', 'descripcion': 'Auriculares Inalámbricos JBL', 'categoria': 'Auricular', 'precio': 60000.0, 'stock': 40},
]

def formatearCodigo(valor):
    return "\t" + str(valor)

def formatearTexto(valor):
    return '"' + str(valor).replace('"', '""') + '"'

def formatearNumero(valor):
    return str(valor).replace(".", ",")

with open("./csv/listaproductos.csv", "w") as f:
    f.write("Codigo;Descripcion;Categoria;Precio;Stock\n")
    for prod in listaProductos:
        f.write(formatearCodigo(prod["codigo"]) + ";")
        f.write(formatearTexto(prod["descripcion"]) + ";") # "descripcion producto";
        f.write(formatearTexto(prod["categoria"]) + ";")
        f.write(formatearNumero(prod["precio"]) + ";")
        f.write(formatearNumero(prod["stock"]))
        f.write("\n")

