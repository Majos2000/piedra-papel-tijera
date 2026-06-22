import random

opciones = ["PIEDRA", "PAPEL", "TIJERA"]

seguir_jugando = True

while seguir_jugando:

    print()
    print("=========================================")
    print("       PIEDRA, PAPEL Y TIJERA")
    print("=========================================")
    print("Elige una opcion:")
    print("  1. Piedra")
    print("  2. Papel")
    print("  3. Tijera")

    # Se pide la opcion al usuario y se valida que no ingrese otra cosa
    opcion_valida = False
    while not opcion_valida:
        entrada = input("Tu opcion (1, 2 o 3): ").strip().upper()
        if entrada == "1" or entrada == "2" or entrada == "3":
            opcion_valida = True
        else:
            print("Entrada invalida. Debes escribir 1, 2 o 3.")

    if entrada == "1":
        usuario = "PIEDRA"
    elif entrada == "2":
        usuario = "PAPEL"
    else:
        usuario = "TIJERA"

    # La computadora elige una opcion al azar
    computadora = random.choice(opciones)

    print()
    print("Tu elegiste     :", usuario)
    print("La computadora  :", computadora)

    if usuario == computadora:
        print("Resultado: EMPATE")
    elif usuario == "PIEDRA" and computadora == "TIJERA":
        print("Resultado: GANASTE")
    elif usuario == "PAPEL" and computadora == "PIEDRA":
        print("Resultado: GANASTE")
    elif usuario == "TIJERA" and computadora == "PAPEL":
        print("Resultado: GANASTE")
    else:
        print("Resultado: GANO LA COMPUTADORA")

    # Se pide al usuario si desea jugar de nuevo y se valida que no ingrese otra cosa
    respuesta_valida = False
    while not respuesta_valida:
        respuesta = input("Deseas jugar de nuevo? (si / no): ").strip().upper()
        if respuesta == "SI" or respuesta == "NO":
            respuesta_valida = True
        else:
            print("Respuesta invalida. Debes escribir 'si' o 'no'.")

    if respuesta == "NO":
        seguir_jugando = False

print()
print("Gracias por jugar.")
