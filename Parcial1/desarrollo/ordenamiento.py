def ordenamiento(lista):
    for i in range(len(lista) -1):
        imin = i
        for j in range(i +1, len(lista)):
            if  lista[j] < lista[imin]:
                imin = j
        print(i, imin, lista)
        lista[i], lista[imin] = lista[imin], lista[i]
    

valores = [50, 60, 20, 30, 10, 40]
ordenamiento(valores)


