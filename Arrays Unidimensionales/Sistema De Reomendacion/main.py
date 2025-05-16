def productos_en_comun(lista1, lista2):
    return list(set(lista1) & set(lista2))

def productos_exclusivos(lista1, lista2):
    exclusivos1 = list(set(lista1) - set(lista2))
    exclusivos2 = list(set(lista2) - set(lista1))
    return exclusivos1, exclusivos2

def catalogo_total(lista1, lista2):
    return list(set(lista1) | set(lista2))

def recomendar(usuario, propios, otros):
    # Recomienda productos que el otro usuario compró y este no
    return list(set(otros) - set(propios))

def mostrar_resultados(lista1, lista2):
    print("Historial Usuario 1:", lista1)
    print("Historial Usuario 2:", lista2)
    print("\n 1 Productos en común:", productos_en_comun(lista1, lista2))
    exclusivos1, exclusivos2 = productos_exclusivos(lista1, lista2)
    print("2 Productos exclusivos de Usuario 1:", exclusivos1)
    print("   Productos exclusivos de Usuario 2:", exclusivos2)
    print("3 Catálogo total de productos:", catalogo_total(lista1, lista2))
    print("4 Recomendaciones para Usuario 1:", recomendar(1, lista1, lista2))
    print("   Recomendaciones para Usuario 2:", recomendar(2, lista2, lista1))

def ingresar_lista(usuario):
    productos = input(f"Ingrese los productos comprados por Usuario {usuario} (separados por coma): ")
    return [p.strip() for p in productos.split(",") if p.strip()]

def main():
    print("Sistema de Recomendación de Productos\n")
    opcion = input("¿Desea ingresar los historiales manualmente? (s/n): ").lower()
    if opcion == "s":
        lista1 = ingresar_lista(1)
        lista2 = ingresar_lista(2)
    else:
        # Listas predefinidas de ejemplo
        lista1 = ["notebook", "mouse", "teclado", "monitor"]
        lista2 = ["monitor", "impresora", "mouse", "parlantes"]
    mostrar_resultados(lista1, lista2)

if __name__ == "__main__":
    main()