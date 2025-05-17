def buscar_secuencias_pares(matriz):
    secuencias = []
    for idx, fila in enumerate(matriz):
        i = 0
        while i < len(fila):
            if fila[i] % 2 == 0:
                inicio = i
                while i + 1 < len(fila) and fila[i + 1] % 2 == 0:
                    i += 1
                if i - inicio + 1 >= 2:
                    secuencias.append({
                        "fila": idx + 1,
                        "inicio": inicio + 1,
                        "fin": i + 1,
                        "longitud": i - inicio + 1,
                        "secuencia": fila[inicio:i+1]
                    })
            i += 1
    return secuencias

def mostrar_resultados_secuencias(secuencias):
    if not secuencias:
        print(" NO EXISTEN NÚMEROS CONSECUTIVOS PARES")
        return
    print(" EXISTEN NÚMEROS CONSECUTIVOS PARES")
    print(f"Cantidad de secuencias encontradas: {len(secuencias)}")
    # Secuencia más corta
    min_len = min(secuencias, key=lambda x: x["longitud"])
    print(f"\nSecuencia más corta (longitud {min_len['longitud']}): {min_len['secuencia']} (Fila {min_len['fila']}, columnas {min_len['inicio']} a {min_len['fin']})")
    # Secuencia más larga
    max_len = max(secuencias, key=lambda x: x["longitud"])
    print(f"Secuencia más larga (longitud {max_len['longitud']}): {max_len['secuencia']} (Fila {max_len['fila']}, columnas {max_len['inicio']} a {max_len['fin']})")
    # Listado de todas las secuencias
    print("\nDetalle de todas las secuencias encontradas:")
    for s in secuencias:
        print(f"Fila {s['fila']}, columnas {s['inicio']} a {s['fin']}: {s['secuencia']}")