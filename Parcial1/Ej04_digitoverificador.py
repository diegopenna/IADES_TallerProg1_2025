"""
Realizar un programa que solicite un numero de 10 digitos y calcule un digito verificador.
Validacion de entrada:
- Se debe validar que el número ingresado se de longitud 10.
- Que todos los caracteres sean números.
Calculo del Digito verificador
- Para calcular el digito verificador se debe multiplicar cada uno de los 10 dígitos por 5, 4, 3, 2, 7, 6, 5, 4, 3, 2  
(Ej: El primer digito se multiplica por 5 , el segundo por 4, el tercero por 3 ....)
- Sumar los valores obtenidos
- Calcular el resto de la división del resultado por 11 (%)
- Restar 11 por el numero obtenido
Ese es el resultado del código verificador 
"""

def digitoVerif(valor):
    valor = str(valor)
    if len(valor) != 10:
        return "El Numero ingresado debe tener 10 digitos."
    
    for c in valor:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return "El Numero ingresado solo deben ser digitos del 0 al 9."
    
    lista = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    suma = []
    # multiplico
    for i in range(10):
        suma.append(lista[i] * int(valor[i]))
    
    # sumo

    total = 0
    for numero in suma:
        total = total + numero
    
    #calculo resto
    resto = total % 11
    
    #Resto 11
    dig = 11 - resto

    return dig



print(digitoVerif("2040541630"))
print(digitoVerif("2026620884"))