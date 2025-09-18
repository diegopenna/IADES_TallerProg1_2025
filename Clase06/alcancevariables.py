def bienvenido():
    print("Bienvenido", lenguaje)

def bienvenidoLocal():
    lenguaje = "Java"
    print("Bienvenido local", lenguaje)

def bienvenidoGlobal():
    global lenguaje
    lenguaje = "Java"
    print("Bienvenido global", lenguaje)

lenguaje = "Python"

print()
bienvenido()
print(lenguaje)

print()
bienvenidoLocal()
print(lenguaje)

print()
bienvenidoGlobal()
print(lenguaje)
