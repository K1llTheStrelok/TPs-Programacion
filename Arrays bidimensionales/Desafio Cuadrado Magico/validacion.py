def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{x:3}" for x in fila))

def es_cuadrado_magico(matriz):
    n = len(matriz)
    magic = n * (n*n + 1) // 2

    # Suma de filas
    for fila in matriz:
        if sum(fila) != magic:
            return False

    # Suma de columnas
    for col in range(n):
        if sum(matriz[f][col] for f in range(n)) != magic:
            return False

    # Diagonal principal
    if sum(matriz[i][i] for i in range(n)) != magic:
        return False

    # Diagonal secundaria
    if sum(matriz[i][n-1-i] for i in range(n)) != magic:
        return False

    return True