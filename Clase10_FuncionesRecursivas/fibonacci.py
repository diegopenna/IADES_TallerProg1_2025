def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva.

    Args:
        n (int): Índice del número de Fibonacci (0-indexado).

    Returns:
        int: El n-ésimo número de Fibonacci.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def secuenciaFibonacci(n):
    """Genera una lista con los primeros n números de Fibonacci.

    Args:
        n (int): Cantidad de números de Fibonacci a generar.

    Returns:
        list: Lista con los primeros n números de Fibonacci.
    """
    lista = []
    for i in range(n):
        lista = lista + [fibonacci(i)]

    return lista

def secuenciaFibonacci2(n):
    rtrn = []

    for i in range(n):
        if i == 0:
            rtrn.append(0)
        elif i == 1:
            rtrn.append(1)
        else:
            rtrn.append(rtrn[i-1] + rtrn[i-2])
    return rtrn


for i in range(10):
    print(fibonacci(i), end=", ")

print()
print(secuenciaFibonacci(10))
print(secuenciaFibonacci2(10))
