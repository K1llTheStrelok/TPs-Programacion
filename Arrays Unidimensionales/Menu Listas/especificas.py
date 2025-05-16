def contar_positivos_negativos(numeros):
    positivos = sum(1 for num in numeros if num > 0)
    negativos = sum(1 for num in numeros if num < 0)
    return positivos, negativos

def suma_pares(numeros):
    return sum(num for num in numeros if num % 2 == 0)

def mayor_impar(numeros):
    impares = [num for num in numeros if num % 2 != 0]
    return max(impares) if impares else "No hay números impares."