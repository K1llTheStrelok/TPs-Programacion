from input import ingresar_datos
from especificas import contar_positivos_negativos, suma_pares, mayor_impar
from array_generales import listar_numeros, listar_pares, listar_posiciones_impares

def menu():
    print("\nMenú de Opciones:")
    print("1. Ingresar datos")
    print("2. Cantidad de positivos y negativos")
    print("3. Suma de los números pares")
    print("4. Mayor número impar")
    print("5. Listar los números ingresados")
    print("6. Listar los números pares")
    print("7. Listar los números en posiciones impares")
    print("8. Salir")

def main():
    numeros = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            numeros = ingresar_datos()
        elif opcion == "2":
            if numeros:
                positivos, negativos = contar_positivos_negativos(numeros)
                print(f"Positivos: {positivos}, Negativos: {negativos}")
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "3":
            if numeros:
                print(f"Suma de los números pares: {suma_pares(numeros)}")
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "4":
            if numeros:
                print(f"Mayor número impar: {mayor_impar(numeros)}")
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "5":
            if numeros:
                listar_numeros(numeros)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "6":
            if numeros:
                listar_pares(numeros)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "7":
            if numeros:
                listar_posiciones_impares(numeros)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()