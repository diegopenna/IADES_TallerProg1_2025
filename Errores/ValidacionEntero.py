def inputEntero(texto):
    while True:
        try:
            valor = int(input(texto))
        except ValueError:
            print("Solo se permiten numeros")
        else:
            return valor


valorEntero = inputEntero("Ingrese Numero: ")