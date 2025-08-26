

print("Valentina".lower())
print("Valentina".lower() > "aaron".lower())

cadena = "Esto es una cadena" 
lista = cadena.split(" ")
print(lista)

fecha = "19/08/2025"
listaFecha = fecha.split("/")
print("Dia: " + listaFecha[0] + " Mes: " +  listaFecha[1] + " Año: " + listaFecha[2])
print("Dia: " + fecha[:2] + " Mes: " +  fecha[3:5] + " Año: " + fecha[-4:])

lista = ["Diego", "Fernanda", "Lucas", "Marcos"]

nombres = ""
for i in range(len(lista)):
    nombres = nombres + lista[i]  + "; "
# "" + "Diego" + "Fernanda" + "Lucas" + "Marcos"
print(nombres[0:-2])





