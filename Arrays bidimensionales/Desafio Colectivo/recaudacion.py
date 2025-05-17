from legajos import validar_legajo

def cargar_recaudacion(legajos, recaudaciones):
    try:
        legajo = int(input("Ingrese su número de legajo: "))
    except ValueError:
        print("Legajo inválido.")
        return
    if not validar_legajo(legajos, legajo):
        print("Legajo no encontrado.")
        return
    try:
        linea = int(input("Ingrese línea (1-3): ")) - 1
        coche = int(input("Ingrese coche (1-5): ")) - 1
        if not (0 <= linea < 3 and 0 <= coche < 5):
            print("Línea o coche fuera de rango.")
            return
        monto = float(input("Ingrese recaudación: "))
        if monto < 0:
            print("No se permiten valores negativos.")
            return
    except ValueError:
        print("Entrada inválida.")
        return
    recaudaciones[linea][coche] += monto
    print("Recaudación registrada.")

def mostrar_matriz_recaudacion(recaudaciones):
    print("\nRecaudación por línea y coche:")
    print("      ", end="")
    for c in range(5):
        print(f"Coche {c+1:>6}", end="")
    print()
    for i, fila in enumerate(recaudaciones):
        print(f"Línea {i+1}", end=" ")
        for monto in fila:
            print(f"{monto:10.2f}", end="")
        print()

def recaudacion_por_linea(recaudaciones):
    print("\nRecaudación total por línea:")
    for i, fila in enumerate(recaudaciones):
        print(f"Línea {i+1}: {sum(fila):.2f}")

def recaudacion_por_coche(recaudaciones):
    try:
        coche = int(input("Ingrese el número de coche (1-5): ")) - 1
        if not (0 <= coche < 5):
            print("Coche fuera de rango.")
            return
    except ValueError:
        print("Entrada inválida.")
        return
    total = sum(recaudaciones[linea][coche] for linea in range(3))
    print(f"Recaudación total del coche {coche+1}: {total:.2f}")

def recaudacion_total(recaudaciones):
    total = sum(sum(fila) for fila in recaudaciones)
    print(f"\nRecaudación total general: {total:.2f}")