
listaProductos = [
    {'codigo': '00017', 'descripcion': 'Disco Rígido WD Blue 1TB', 'categoria': 'Almacenamiento', 'subcategoria': 'Disco Duro', 'precio': 90000.0, 'stock': 30},
    {'codigo': '00020', 'descripcion': 'Tarjeta MicroSD Samsung 128GB', 'categoria': 'Almacenamiento', 'subcategoria': 'Memoria Flash', 'precio': 35000.0, 'stock': 40},
    {'codigo': '00018', 'descripcion': 'SSD Kingston A400 480GB', 'categoria': 'Almacenamiento', 'subcategoria': 'SSD', 'precio': 85000.0, 'stock': 25},
    {'codigo': '00019', 'descripcion': 'Pendrive Sandisk 64GB', 'categoria': 'Almacenamiento', 'subcategoria': 'USB', 'precio': 20000.0, 'stock': 60},
    {'codigo': '00030', 'descripcion': 'Auriculares Inalámbricos JBL', 'categoria': 'Auricular', 'subcategoria': 'Bluetooth', 'precio': 60000.0, 'stock': 40},
    {'codigo': '00029', 'descripcion': 'Cable HDMI 2m', 'categoria': 'Cable', 'subcategoria': 'Video', 'precio': 7000.0, 'stock': 70},
    {'codigo': '00028', 'descripcion': 'Cable USB-C a USB 1m', 'categoria': 'Cable', 'subcategoria': 'Datos', 'precio': 5000.0, 'stock': 80},
    {'codigo': '00027', 'descripcion': 'Cargador Apple 20W USB-C', 'categoria': 'Cargador', 'subcategoria': 'Celular', 'precio': 35000.0, 'stock': 35},
    {'codigo': '00026', 'descripcion': 'Cargador Motorola TurboPower', 'categoria': 'Cargador', 'subcategoria': 'Celular', 'precio': 22000.0, 'stock': 45},
    {'codigo': '00025', 'descripcion': 'Cargador Samsung 25W', 'categoria': 'Cargador', 'subcategoria': 'Celular', 'precio': 20000.0, 'stock': 50},
    {'codigo': '00003', 'descripcion': 'iPhone 13', 'categoria': 'Celular', 'subcategoria': 'Gama Alta', 'precio': 1500000.0, 'stock': 15},
    {'codigo': '00002', 'descripcion': 'Motorola G10', 'categoria': 'Celular', 'subcategoria': 'Gama Baja', 'precio': 800000.0, 'stock': 20},
    {'codigo': '00001', 'descripcion': 'Samsung A22', 'categoria': 'Celular', 'subcategoria': 'Gama Media', 'precio': 500000.0, 'stock': 30},
    {'codigo': '00004', 'descripcion': 'Xiaomi Redmi Note 11', 'categoria': 'Celular', 'subcategoria': 'Gama Media', 'precio': 600000.0, 'stock': 25},
    {'codigo': '00021', 'descripcion': 'Funda iPhone 13 Transparente', 'categoria': 'Funda', 'subcategoria': 'Celular', 'precio': 5000.0, 'stock': 70},
    {'codigo': '00022', 'descripcion': 'Funda Samsung A22 Negra', 'categoria': 'Funda', 'subcategoria': 'Celular', 'precio': 4500.0, 'stock': 60},
    {'codigo': '00024', 'descripcion': 'Funda Notebook 15.6"', 'categoria': 'Funda', 'subcategoria': 'Notebook', 'precio': 15000.0, 'stock': 30},
    {'codigo': '00023', 'descripcion': 'Funda Universal Tablet 10"', 'categoria': 'Funda', 'subcategoria': 'Tablet', 'precio': 8000.0, 'stock': 40},
    {'codigo': '00007', 'descripcion': 'Notebook Dell Inspiron 14', 'categoria': 'Notebook', 'subcategoria': 'Trabajo', 'precio': 1400000.0, 'stock': 8},
    {'codigo': '00006', 'descripcion': 'Notebook HP Pavilion 15', 'categoria': 'Notebook', 'subcategoria': 'Trabajo', 'precio': 1350000.0, 'stock': 10},
    {'codigo': '00008', 'descripcion': 'Notebook Asus VivoBook', 'categoria': 'Notebook', 'subcategoria': 'Hogar', 'precio': 1250000.0, 'stock': 9},
    {'codigo': '00005', 'descripcion': 'Notebook Lenovo IdeaPad 3', 'categoria': 'Notebook', 'subcategoria': 'Hogar', 'precio': 1200000.0, 'stock': 12},
    {'codigo': '00016', 'descripcion': 'Impresora HP DeskJet 2710', 'categoria': 'Periférico', 'subcategoria': 'Salida', 'precio': 120000.0, 'stock': 15},
    {'codigo': '00015', 'descripcion': 'Monitor Samsung 24"', 'categoria': 'Periférico', 'subcategoria': 'Salida', 'precio': 180000.0, 'stock': 20},
    {'codigo': '00013', 'descripcion': 'Mouse Logitech M170', 'categoria': 'Periférico', 'subcategoria': 'Entrada', 'precio': 15000.0, 'stock': 100},
    {'codigo': '00014', 'descripcion': 'Teclado Redragon Kumara', 'categoria': 'Periférico', 'subcategoria': 'Entrada', 'precio': 45000.0, 'stock': 50},
    {'codigo': '00010', 'descripcion': 'iPad 9na Generación', 'categoria': 'Tablet', 'subcategoria': 'iOS', 'precio': 1100000.0, 'stock': 14},
    {'codigo': '00009', 'descripcion': 'Tablet Samsung Galaxy Tab A7', 'categoria': 'Tablet', 'subcategoria': 'Android', 'precio': 700000.0, 'stock': 18},
    {'codigo': '00011', 'descripcion': 'Tablet Lenovo Tab M10', 'categoria': 'Tablet', 'subcategoria': 'Android', 'precio': 650000.0, 'stock': 20},
    {'codigo': '00012', 'descripcion': 'Tablet Huawei MatePad T10', 'categoria': 'Tablet', 'subcategoria': 'Android', 'precio': 680000.0, 'stock': 16},
]

i = 0
cantidad = len(listaProductos)

while i < cantidad:
    categoriaActual = listaProductos[i]["categoria"]
    totalCat = 0 
    while i < cantidad and categoriaActual == listaProductos[i]["categoria"]:
        totalCat = totalCat + listaProductos[i]["precio"]
        i += 1 
    print("Total de precio de", categoriaActual,":", totalCat)   
    #print(listaProductos[i])
    
