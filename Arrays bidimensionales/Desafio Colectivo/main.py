from legajos import generar_legajos, validar_legajo
from recaudacion import (
    cargar_recaudacion, mostrar_matriz_recaudacion,
    recaudacion_por_linea, recaudacion_por_coche, recaudacion_total
)

def menu():
    print("\n--- Menú de Gestión de Recaudaciones ---")
    print("1. Cargar planilla de recaudación")
    print("2. Mostrar recaudación de cada coche y línea")
    print("3. Calcular y mostrar recaudación por línea")
    print("4. Calcular y mostrar recaudación por coche")
    print("5. Calcular y mostrar recaudación total")
    print("6. Salir")

def main():
    legajos = generar_legajos(15)
    recaudaciones = [[0 for _ in range(5)] for _ in range(3)]  # 3 líneas x 5 coches

    print("Legajos de choferes:", legajos)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cargar_recaudacion(legajos, recaudaciones)
        elif opcion == "2":
            mostrar_matriz_recaudacion(recaudaciones)
        elif opcion == "3":
            recaudacion_por_linea(recaudaciones)
        elif opcion == "4":
            recaudacion_por_coche(recaudaciones)
        elif opcion == "5":
            recaudacion_total(recaudaciones)
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()