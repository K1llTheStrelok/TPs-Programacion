from input import ingresar_matriz, generar_matriz_aleatoria, mostrar_matriz
from secuencias import (
    buscar_secuencias_pares, 
    mostrar_resultados_secuencias
)

def menu():
    print("\n--- Menú de Análisis de Secuencias Pares ---")
    print("1. Ingresar matriz manualmente")
    print("2. Generar matriz aleatoria")
    print("3. Analizar secuencias de números consecutivos pares")
    print("4. Salir")

def main():
    matriz = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            matriz = ingresar_matriz()
            mostrar_matriz(matriz)
        elif opcion == "2":
            matriz = generar_matriz_aleatoria()
            mostrar_matriz(matriz)
        elif opcion == "3":
            if not matriz:
                print("Primero debe ingresar o generar una matriz.")
            else:
                secuencias = buscar_secuencias_pares(matriz)
                mostrar_resultados_secuencias(secuencias)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()