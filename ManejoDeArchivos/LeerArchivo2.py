listaPaises = []
archPaises = open("ManejoDeArchivos\paises.list", "r", encoding="utf8")
while True:
    linea = archPaises.readline()
    if linea == "":
        break
    else:
        listaPaises.append(linea.strip())
archPaises.close()


while True:
    pais = input("Ingrese un pais:")
    listaPaises.append(pais)
    opc = input("Desea Agregar otro pais? s/n:")
    if opc.lower() == "n":
        break

for pais in listaPaises:
    print(pais)

archPaises = open("ManejoDeArchivos\paises.list", "w")
for pais in listaPaises:
    archPaises.write(f"{pais}\n")

archPaises.close()

