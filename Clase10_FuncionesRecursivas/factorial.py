def factorial(n):
    """Calcula el factorial de un número de forma recursiva.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: Factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial de 5:", factorial(5))