"""
Autor: Carlos Gonzalez Rubio
Fecha inicio: 20/11/2024
Fecha final:

ACTIVIDAD 1: INTRODUCCIÓN A PYTHON

Se pretende disponer de una pequeña aplicación realizada con Python para gestionar las estadísticas de los jugadores de
un equipo de baloncesto en un partido.
"""
import time

# APARTADO FUNCIONES --------------------------------------------------------------------

# ===================================================================
# Se define el menú interactivo. Se permite la escalabilidad de este.
# ===================================================================
def menu():
    print("""
    ====================================
    Tiene estas opciones para realizar:
    ====================================
    """)
    titulos = ["Salir del Programa",
               "Introducir un nuevo jugador",
               "Listar jugadores",
               "Máximo anotador",
               "Estadísticas del equipo"]  # Lista de opciones del usuario
    contador_titulos = 0  # Contador para índices

    # Bucle for para imprimir cada título de la lista con su número correspondiente
    for titulo in titulos:
        if contador_titulos < len(titulos) - 1:
            contador_titulos += 1
            print(f"[{contador_titulos}] {titulos[contador_titulos]}")
        else:
            contador_titulos = 0
            print(f"[{contador_titulos}] {titulos[contador_titulos]}")

    decision = input("Elija el número que desea realizar: ")
    return decision

# ===================================================================
# Saludo inicial al usuario
# ===================================================================
def saludo():
    print("¡Bienvenido!")
    nombre = input("Dime tu nombre: ")
    decision = input(f"¿Desea iniciar sesión, {nombre}? [Si/No]\n").lower()
    return decision

# ===================================================================
# OPCIÓN 1. Introducir nuevo jugador
# ===================================================================
def nuevo_jugador(lista_caracteristicas):
    jugador = {"Nombre": lista_caracteristicas[0],
               "Dorsal": lista_caracteristicas[1],
               "Canastas de 3": lista_caracteristicas[2],
               "Canastas de 2": lista_caracteristicas[3],
               "Canastas de 1": lista_caracteristicas[4]}
    return jugador

# Variables globales ------------------------------------------------
listado_jugadores = []  # Lista para almacenar los jugadores

# Saludo inicial -----------------------------------------------------
decision = saludo()  # Saluda al usuario y pregunta si quiere iniciar sesión

# BUCLE PRINCIPAL
while True:
    # Si la decisión es "no", termina el programa
    if decision == "no":
        print("Espero verte de nuevo...")
        break

    # Si la decisión es "sí", inicia el menú de opciones
    elif decision == "si":
        opcion = menu()

        if opcion == "1":
            print("\n--- Agregar un nuevo jugador ---")
            lista_caracteristicas = [input("Indique nombre del jugador: "),
                                     input("Indique dorsal del jugador: "),
                                     input("Indique canastas de 3 del jugador: "),
                                     input("Indique canastas de 2 del jugador: "),
                                     input("Indique canastas de 1 del jugador: ")]

            jugador = nuevo_jugador(lista_caracteristicas)
            listado_jugadores.append(jugador)

            print("\nJugador agregado correctamente.")

        elif opcion == "2":
            if not listado_jugadores:
                print("\nNo hay jugadores registrados aún.")
            else:
                print("\nListado de jugadores:")
                for j in listado_jugadores:
                    print(f"Nombre: {j['Nombre']}, Dorsal: {j['Dorsal']}, Canastas 3: {j['Canastas de 3']}, "
                          f"Canastas 2: {j['Canastas de 2']}, Canastas 1: {j['Canastas de 1']}")

        elif opcion == "0":
            print("¡Gracias por usar la aplicación! Hasta pronto.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")
    else:
        print("Entrada inválida. Responda 'Si' o 'No'.")
        decision = saludo()  # Re-pregunta si la entrada inicial fue inválida
