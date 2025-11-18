def division(num1, num2):
    try:
        result = None
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
    except ZeroDivisionError:
        print ("No se puede dividir por cero")
    except ValueError:
        print ("Los valores ingresados son incorrectos.")
    else:
        print("No se produjo error")
    
    return result



valor1 = input("Ingrese un numero: ")
valor2 = input("Ingrese otro numero distinto a cero: ")

print("Resultado:", division(valor1, valor2))