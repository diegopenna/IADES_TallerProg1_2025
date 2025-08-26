import random


##Usando sample
#numeroOculto = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4 )
#numeroOculto = ''.join(numeroOculto)

print("Juego del Numero oculto")
print()


numeroInvalido = True

while numeroInvalido:
    numeroOculto =  random.randrange(10000)
    numeroOculto = str(numeroOculto)
    numeroOculto = "000" + numeroOculto
    numeroOculto = numeroOculto[-4:]
    #tenemos un numero de 4 digitos
    numeroInvalido = False
    for i in range(3):
        digitoActual = numeroOculto[i]
        subcadena = numeroOculto[i+1:]
        if (digitoActual in subcadena):
            numeroInvalido = True
            break

print(numeroOculto)


while True:
    numero = input("Ingrese un numero:")
    caracteresPermitidos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #valido que sean 4 digitos
    numeroInvalido = (len(numero) != 4)

    if (numeroInvalido):
        print("El numero debe tener 4 digitos.")
        continue

    #valido que sean todos numeros
    numeroInvalido = False
    for c in numero:
        if c not in caracteresPermitidos:
            numeroInvalido = True
            break 
    
    if numeroInvalido:
        print("Solo esta permitido el ingreso de numeros")
        continue
    
    #validar que no se repitan
    numeroInvalido = False
    for i in range(3):
        digitoActual = numero[i]
        subcadena = numero[i+1:]
        if (digitoActual in subcadena):
            numeroInvalido = True
            break
    
    if numeroInvalido:
        print("El numero no tiene que tener digitos repetidos")
        continue
    else:
        break
    
print(numeroInvalido)


#-numero tenga 4 digitos
#-*que los 4 digitos sean numeros
#-que los 4 digitos no se repitan





