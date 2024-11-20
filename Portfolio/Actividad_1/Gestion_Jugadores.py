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


# CICLO DE PROGRAMA -----------------------------------------------------------------------

decision = saludo()  # guarda la decisión del usuario
while True:
    if decision == "si":  # condición del usuario si acepta o no iniciar sesión

        try:
            opcion_elegida = int(menu())  # guarda la opción elegida del usuario

        except ValueError:
            print("Debe ser un número, vuelva a intentarlo")
            time.sleep(2)
            pass

        else:
            if opcion_elegida == 0:
                print("¡Espero verte pronto!")
                time.sleep(2)
                break


