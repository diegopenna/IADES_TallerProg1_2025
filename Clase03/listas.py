lista = [1, ["pepe", 3], "lalala"]

print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(len(lista[1]))
print("Ultimo indice:", len(lista) -1)
print("Ultimo Elemento:", lista[len(lista) -1])
print("Ultimo Elemento:", lista[-1])

otraLista = list("Python")
print(otraLista)
print(list((1, 2, 3)))

#sublistas
print(otraLista[:-3])
print(otraLista[0:6:2])

