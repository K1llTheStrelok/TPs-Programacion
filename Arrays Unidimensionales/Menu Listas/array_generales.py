def listar_numeros(numeros):
    print("Números ingresados:", numeros)

def listar_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    print("Números pares:", pares)

def listar_posiciones_impares(numeros):
    posiciones_impares = [numeros[i] for i in range(len(numeros)) if i % 2 != 0]
    print("Números en posiciones impares:", posiciones_impares)