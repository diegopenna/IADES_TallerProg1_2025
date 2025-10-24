f = open("texto.txt", "r")

while True:
    linea = f.readline()
    if not linea:
        break
    else:
        print(linea)

f.close()

f = open("texto.txt", "r")

linea = f.readline()
print(linea)

f.close()

