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
               "Estadísticas del equipo"]   # lista de opciones del usuario
    contador_titulos = 0  # contador para indices

    # Bucle for para imprimir cada titulo de la lista con su número correspondiente
    for titulo in titulos:

        # estas condiciones hacen que salir del programa siempre sea la ultima opción
        if contador_titulos < len(titulos)-1:
            contador_titulos += 1
            print(f"[{contador_titulos}] {titulos[contador_titulos]}")
        else:
            contador_titulos = 0
            print(f"[{contador_titulos}] {titulos[contador_titulos]}")

    decision = input("Elija el número que desea realizar: ")
    return decision

# ===================================================================
# Saludo inicial al usuario, permite minusculas, no acentos
# ===================================================================
def saludo():
    print("¡Bienvenido!")
    nombre = input("Dime tu nombre: ")
    decision = input(f"¿Desea iniciar sesión, {nombre}? [Si/No]\n").lower()
    return decision

# ===================================================================
# OPCIÓN 1. Introducir nuevo jugador
# ===================================================================
def nuevo_jugador(nombre, dorsal, Canastas_3, Canastas_2, Canastas_1):
    lista_juadores = []
    jugador = {"Nombre": nombre, "Dorsal": dorsal, "Canastas de 3": Canastas_3,
               "Canastas de 2": Canastas_2, "Canatas de 1": Canastas_1}
    lista_juadores.append(jugador)
    return lista_juadores

# CICLO DE PROGRAMA -----------------------------------------------------------------------

decision = saludo()  # guarda la decisión del usuario

while True:

    if decision == "no":  # decisión "No" del usuario
        print("Una pena... Nos vemos en la próxima")
        break

    elif decision == "si":  # condición del usuario si acepta o no iniciar sesión

        # ---------------------------------------------------------------------
        # Bloque validación entrada de usuario
        try:
            opcion_elegida = int(menu())  # guarda la opción elegida del usuario

        # Para valores incorrectos
        except ValueError:
            print("Debe ser un número, vuelva a intentarlo")
            time.sleep(2)
            pass
        # Para valores correctos
        else:
            if opcion_elegida == 0:
                print("¡Espero verte pronto!")
                time.sleep(2)
                break

            if opcion_elegida == 1:
                nombre = input("Nombre del jugador: ")
                dorsal = input("Dorsal del jugador: ")
                Canastas_3 = input("Número de canastas de 3: ")
                Canastas_2 = input("Número de canastas de 2: ")
                Canastas_1 = input("Número de canastas de 1: ")
                jugadores_listados = nuevo_jugador(nombre, dorsal, Canastas_3,
                                                  Canastas_2, Canastas_1)
                print("¡Jugador creado!")
                time.sleep(0.5)

        # ---------------------------------------------------------------------

