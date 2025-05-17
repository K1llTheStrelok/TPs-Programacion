import random

def generar_legajos(cantidad):
    legajos = set()
    while len(legajos) < cantidad:
        legajo = random.randint(1000, 9999)
        legajos.add(legajo)
    return list(legajos)

def validar_legajo(legajos, legajo):
    return legajo in legajos