#Importar la libreria entera
#import math as lib
#importar funciones especificas de la libreria
from math import sqrt
from math import log as funcionLogaritmo

def cuadrado(valor):
    calculo = valor ** 2
    #calculo = valor * valor
    return calculo

def calculo(valor1, valor2, valor3):
    aux = valor1 + (valor2 * valor3)
    print("Resultado:", aux)
    return aux

x = 2
print("La raiz cuadrada es:", sqrt(x))
print("El logaritmo es:", funcionLogaritmo(x, 10))
print("El cuadrado es:", cuadrado(x))
print(calculo(10, 3, 4))
print(calculo(valor3=4, valor1=10, valor2=3))
print(calculo(10,valor3=4, valor2= 3))
print("Hola", "Como", "Estas", end="#")

calculo(12, 1, 3)

