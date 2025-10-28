archPaises = open("ManejoDeArchivos\paises.list", "r", encoding="utf8")
listaPaises = archPaises.readlines()
archPaises.close()

print("Antes de stripear:")
print(listaPaises)
for i in range(len(listaPaises)):
    listaPaises[i] = listaPaises[i].strip()
print("Despues de stripear:")
print(listaPaises)

for pais in listaPaises:
    print(pais)
