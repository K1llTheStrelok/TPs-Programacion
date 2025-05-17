import random

def pedir_entero(mensaje):
    valor = input(mensaje)
    while not (valor.lstrip('-').isdigit()):
        print("Debe ingresar un número entero.")
        valor = input(mensaje)
    return int(valor)

def ingresar_matriz():
    filas = pedir_entero("Ingrese la cantidad de filas: ")
    columnas = pedir_entero("Ingrese la cantidad de columnas: ")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            val = pedir_entero(f"Ingrese el valor para [{i+1},{j+1}]: ")
            fila.append(val)
        matriz.append(fila)
    return matriz

def generar_matriz_aleatoria():
    filas = pedir_entero("Ingrese la cantidad de filas: ")
    columnas = pedir_entero("Ingrese la cantidad de columnas: ")
    matriz = [
        [random.randint(1, 100) for _ in range(columnas)]
        for _ in range(filas)
    ]
    print("Matriz generada aleatoriamente:")
    return matriz

def mostrar_matriz(matriz):
    print("\nMatriz actual:")
    for fila in matriz:
        print(" ".join(f"{x:4}" for x in fila))