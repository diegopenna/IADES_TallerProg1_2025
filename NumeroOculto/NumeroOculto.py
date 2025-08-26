import random

numeroOculto = random.randrange(10000)
numeroOculto = str(numeroOculto)
numeroOculto = "000" + numeroOculto
numeroOculto = numeroOculto[-4:]
#tenemos un numero de 4 digitos
print()
print(numeroOculto)
print()

numeroInvalido = False
for i in range(3):
    print(numeroOculto[i+1:])
    if (numeroOculto[i] in numeroOculto[i+1:]):
        numeroInvalido = True
        break

if (numeroInvalido):
    print("Numero incorrecto")




