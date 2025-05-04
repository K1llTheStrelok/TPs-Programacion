import random

def verificar_ganador_ronda(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Jugador"
    else:
        return "Máquina"

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
    if aciertos_jugador == 2 or aciertos_maquina == 2 or ronda_actual >= 3:
        return False
    return True

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "Máquina"
    else:
        return "Empate"

def mostrar_elemento(eleccion):
    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    elif eleccion == 3:
        return "Tijera"
    else:
        return "Elección inválida"

def jugar_piedra_papel_tijera():
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0

    print("Elige: 1 para Piedra, 2 para Papel, 3 para Tijera")

    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
        jugador = input("Tu elección: ")
        if not jugador.isdigit() or int(jugador) not in [1, 2, 3]:
            print("Elige un número válido (1, 2 o 3).")
            continue

        jugador = int(jugador)
        maquina = random.randint(1, 3)
        print(f"Tú eleccion: {mostrar_elemento(jugador)}")
        print(f"Eleccion de la maquina: {mostrar_elemento(maquina)}")

        resultado_ronda = verificar_ganador_ronda(jugador, maquina)
        print(f"Resultado de la ronda: {resultado_ronda}")

        if resultado_ronda == "Jugador":
            aciertos_jugador += 1
        elif resultado_ronda == "Máquina":
            aciertos_maquina += 1

        ronda_actual += 1
        print(f"Puntaje - Jugador: {aciertos_jugador}, Máquina: {aciertos_maquina}")

    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print(f"¡El ganador de la partida es: {ganador}!")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()