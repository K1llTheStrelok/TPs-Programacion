def ingresar_datos():
    numeros = []
    print("Ingrese 10 números enteros entre -1000 y 1000:")
    while len(numeros) < 10:
        try:
            num = int(input(f"Número {len(numeros) + 1}: "))
            if -1000 <= num <= 1000:
                numeros.append(num)
            else:
                print("El número debe estar entre -1000 y 1000.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
    return numeros