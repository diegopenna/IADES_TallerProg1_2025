


lista = list()
lista.append("Rojo")
lista.append("Azul")

print(lista)

lista2 = list(["Amarillo", "Verde"])
print(lista2)


class Marcador:
    def __init__(self, color = "", largo = 0, puntas = 1, nivel= 100):
        self.color = color
        self.largo = largo
        self.puntas = puntas
        self.nivel = nivel


unMarcador = Marcador("Marron", 12, 2, 100)

print(unMarcador.color, unMarcador.largo, unMarcador.puntas, unMarcador.nivel)

otroMarcador = Marcador()
otroMarcador.color = "Negro"

print(otroMarcador.color, otroMarcador.largo, otroMarcador.puntas, otroMarcador.nivel)

marcadorRojo = Marcador("Rojo", nivel=50)

print(marcadorRojo.color, marcadorRojo.largo, marcadorRojo.puntas, marcadorRojo.nivel)
