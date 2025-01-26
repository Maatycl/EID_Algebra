import math

#——— calculo a través del teorema del binomio———
def ciclo_repetitivo(a, b, n):
        """Cálculo usando el ciclo repetitivo basado en el teorema del binomio."""
        suma = 0
        for k in range(n + 1):
            coef_binomial = math.comb(n, k)  # Calcula nCk = n! / (k!(n-k)!)
            suma += coef_binomial * (a ** (n - k)) * (b ** k)
        return suma

#Calcular de forma directa
def binomio_directo(a, b, n):
    binomio = (a + b) ** n

    return binomio