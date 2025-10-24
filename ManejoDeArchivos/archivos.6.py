f = open("texto.txt", "w")
print("Hola como estas", file=f)
print("Por aca todo bien", file=f)
print("Otra lina", file=f)

f.close()

f = open("texto.txt", "r")
#print(f.read())
print(f.readlines())
