def division(num1, num2):
    try:
        result = None
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
    except ValueError:
        print ("Los valores ingresados son incorrectos.")
    else:
        print("No se produjo error")
    
    return result

def promedio(*valores, cantidad):
    suma = 0
    for a in valores:
        suma = suma + a
    
    result = division(suma, cantidad)
    return result 

try:
    prom = promedio(3, 4, 5, 0)
except ZeroDivisionError:
    print("Error de division por cero")
except TypeError:
    print("Falto un parametro")
else:
    print("Resultado:", prom)