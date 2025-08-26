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
    for j in range(i + 1, 4):
        #print("Comparar digito", i , "con digito", j) 
        if (numeroOculto[i] == numeroOculto[j]):
            numeroInvalido = True
            break

if (numeroInvalido):
    print("Numero incorrecto")

#otra manera
numeroInvalido = False
for i in range(3):
    if (numeroOculto[i] in numeroOculto[i+1:]):
        numeroInvalido = True
        break

if (numeroInvalido):
    print("Numero incorrecto")




