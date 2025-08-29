# Obtener Numero aleatoreo de 4 digitos distintos
def obtenerNumeroOculto():
    from random import randrange
    ##Usando sample
    #numeroOculto = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4 )
    #numeroOculto = ''.join(numeroOculto)
    numeroInvalido = True
    while numeroInvalido:
        numeroOculto =  randrange(10000)
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
    return numeroOculto

#Funcion que solicita un numero de 4 digitos distintos
def solicitarNumero():
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
    return numero
 
 
def compararNumeros(numeroBase , numero):
    if numeroBase == numero:
        return '4B 0R 0M'
    buenos = 0
    regulares = 0
    malos = 0
    for i in range(len(numero)):
        encontro = False
        for j in range(len(numeroBase)):
            if numero[i] == numeroBase[j]:
                encontro = True
                if i != j:
                    regulares += 1 # regulares = reagulares + 1
                else:
                    buenos += 1
        if encontro == False:
            malos += 1

    return str(buenos) +"B " + str(regulares) + "R " + str(malos) + "M"

numeroOculto = obtenerNumeroOculto()
print(numeroOculto)

while True: 
    numero = solicitarNumero()
    print(numero)
    resultado = compararNumeros(numeroOculto, numero)
    if resultado == '4B 0R 0M':
        print("Felicitaciones, adivinaste el numero.")
        break
    else:
        print("Numero incorrecto. Resultado:", resultado)







