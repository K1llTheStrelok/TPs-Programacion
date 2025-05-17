import random

def ingresar_matriz(n):
    matriz = []
    usados = set()
    print(f"Ingrese los números del 1 al {n*n}, sin repetir:")
    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                try:
                    val = int(input(f"Elemento [{i+1},{j+1}]: "))
                    if val < 1 or val > n*n:
                        print(f"Debe estar entre 1 y {n*n}.")
                    elif val in usados:
                        print("Número repetido, ingrese otro.")
                    else:
                        fila.append(val)
                        usados.add(val)
                        break
                except ValueError:
                    print("Debe ingresar un número entero.")
        matriz.append(fila)
    return matriz

def generar_matriz_aleatoria(n):
    nums = list(range(1, n*n+1))
    random.shuffle(nums)
    matriz = [nums[i*n:(i+1)*n] for i in range(n)]
    print("Matriz generada aleatoriamente :")
    return matriz