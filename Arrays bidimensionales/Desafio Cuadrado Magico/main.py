from input import ingresar_matriz, generar_matriz_aleatoria
from validacion import es_cuadrado_magico, mostrar_matriz

def main():
    print("=== Verificación de Cuadrado Mágico ===")
    opcion = input("¿Desea ingresar la matriz manualmente (M) o generar una aleatoria (A)? [M/A]: ").strip().upper()
    while opcion not in ("M", "A"):
        opcion = input("Opción inválida. Ingrese 'M' o 'A': ").strip().upper()

    try:
        n = int(input("Ingrese el tamaño n de la matriz (n x n): "))
        if n < 3:
            print("El tamaño debe ser al menos 3.")
            return
    except ValueError:
        print("Debe ingresar un número entero.")
        return

    if opcion == "M":
        matriz = ingresar_matriz(n)
    else:
        matriz = generar_matriz_aleatoria(n)

    print("\nMatriz ingresada:")
    mostrar_matriz(matriz)

    if es_cuadrado_magico(matriz):
        print("\n¡Es un cuadrado mágico!")
    else:
        print("\nNo es un cuadrado mágico.")

if __name__ == "__main__":
    main()