import math
#——— calculo a través del teorema del binomio———
def binomio_directo(a, b, n):
    suma = 0
    for k in range(n + 1):
        coef_binomial = math.comb(n, k)  # Calcula nCk = n! / (k!(n-k)!)
        suma += coef_binomial * (a * (n - k)) * (b * k)
    return suma

#——-calculo a través del ciclo———
def sumatoria_ciclo(a, b, n):
    resultado = 0
    for k in range(n + 1):
        resultado += math.comb(n, k) * (a * (n - k)) * (b * k)
    return resultado

#——-Ingreso del usuario——-
n = int(input("Ingrese el valor de n: "))
a = 1  # Puedes modificar estos valores
b = 1

resultado_directo = binomio_directo(a, b, n)
resultado_ciclo = sumatoria_ciclo(a, b, n)

#——-Mostrar resultados——-
print(f"Resultado usando el teorema del binomio: {resultado_directo}")
print(f"Resultado usando un ciclo repetitivo: {resultado_ciclo}")

#———Comparación——-
if resultado_directo == resultado_ciclo:
    print("¡Los resultados coinciden!")
else:
    print("Hay una discrepancia en los resultados.")