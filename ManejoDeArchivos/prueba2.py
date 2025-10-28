try:
    archPaises = open("ManejoDeArchivos\paises.list")
    listaPaises = archPaises.readlines()
    archPaises.close()
except FileNotFoundError:
    listaPaises = []

print(listaPaises)