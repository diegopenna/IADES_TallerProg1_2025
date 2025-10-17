"""
Realizar un programa que solicite un numero de 10 digitos y calculo un digito verificador.
- Se debe validar que el numero ingresado se de longitud 10.
- Que todos los caracteres sean numeros.
- Para calcular el digito verificador se debe multiplicar cada uno de los 10 digitos por 5, 4, 3, 2, 7, 6, 5, 4, 3, 2
    (El primer digito se multiplica por 5 , el segundo por 4, el tercero por 3 ....)
- Sumar los valores obtenidos
- Calcular el resto de la division del resultado por 11 (%)
- Restar 11 por el numero obtenido
Ese es el resultado del codigo verificador
"""

def digitoVeridicador():
    while True:
        valor = input("Ingrese un numero de 10 digitos")
        if len(valor) != 10:
            print("Longitud del numero incorrecta")
            continue
        esnumero = True
        for c in valor:
            if not(c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
                print("Solo debe ingresar numeros")
                break
        else:
            break
    lista = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i] * int(valor[i])

    resto = suma % 11
    digitoVerif = 11 - resto
    print("El digito verificador es:", digitoVerif)


digitoVeridicador()