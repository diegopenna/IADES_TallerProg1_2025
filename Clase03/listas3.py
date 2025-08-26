l1 = ["manzana", "pera", "babana"]
l2 = ["mandarina", "naranja"]

#l1 = l1 + l2
print(l1 + l2)
print(l1)
print(l2)

l1.append("Frutilla")
print(l1)
l1.insert(2, "Melon")
print(l1)
l1.extend(["Sandia", "Ciruela"])
print(l1)

valor = input("Ingrese fruta a borrar: ")
if (valor in l1):
    l1.remove(valor)
print(l1)

valor = input("Ingrese fruta a sacar: ")
if (valor in l1):
    i = l1.index(valor)
    fruta = l1.pop(i)
    print(fruta)
print(l1)

i = int(input("Ingrese indice a borrar: "))
l1.pop(i)
print(l1)



