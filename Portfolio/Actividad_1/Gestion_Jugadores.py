"""
Autor: Carlos Gonzalez Rubio
Fecha inicio: 20/11/2024
Fecha final:

ACTIVIDAD 1: INTRODUCCIÓN A PYTHON

Se pretende disponer de una pequeña aplicación realizada con Python para gestionar las estadísticas de los jugadores de
un equipo de baloncesto en un partido.
"""

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

    decisiones = input("Elija el número que desea realizar: ")
    return decisiones

# ===================================================================
# Saludo inicial al usuario
# ===================================================================
def saludo():
    print("¡Bienvenido!")
    nombre = input("Dime tu nombre: ")
    decisiones = input(f"¿Desea iniciar sesión, {nombre}? [Si/No]\n").lower()
    return decisiones

# ===================================================================
# OPCIÓN 1. Introducir nuevo jugador
# ===================================================================
def agregar_jugador(listado_jugadores):
    print("\n--- Agregar un nuevo jugador ---")

    # lista de caracteristicas del para enviar a la función
    lista_caracteristicas = [input("Indique nombre del jugador: "),
                             input("Indique dorsal del jugador: "),
                             input("Indique canastas de 3 del jugador: "),
                             input("Indique canastas de 2 del jugador: "),
                             input("Indique canastas de 1 del jugador: ")]

    # llamada a la función de crear jugador
    jugador = nuevo_jugador(lista_caracteristicas)
    # añade el jugador a una lista de jugadores
    listado_jugadores.append(jugador)

    # avisa de que se ha creado el jugador
    print("\nJugador agregado correctamente.")
# ===================================================================
# Subfunción de OPCIÓN 1. Introducir nuevo jugador
# ===================================================================
def nuevo_jugador(lista_caracteristica):
    jugadores = {"Nombre": lista_caracteristica[0],
               "Dorsal": lista_caracteristica[1],
               "Canastas de 3": lista_caracteristica[2],
               "Canastas de 2": lista_caracteristica[3],
               "Canastas de 1": lista_caracteristica[4]}
    return jugadores

# ===================================================================
# OPCIÓN 2. Listar jugadores creados
# ===================================================================
def listar_jugadores(lista_jugadores):
    # si no hay jugadores, avisa al usuario
    if not listado_jugadores:
        print("\nNo hay jugadores registrados aún.")

    # Imprime una cadena f-string por cada jugador de la lista de jugadores con sus caracteristicas
    else:
        print("\nListado de jugadores:")
        for j in listado_jugadores:
            print(f"Nombre: {j['Nombre']}, Dorsal: {j['Dorsal']}, Canastas de 3: {j['Canastas de 3']}, "
                  f"Canastas de 2: {j['Canastas de 2']}, Canastas de 1: {j['Canastas de 1']}")


# ===================================================================
# OPCIÓN 3. Máximo anotador
# ===================================================================
def maximo_anotador(lista_jugadores):

    # Variables generales función =======================
    lista_puntuaciones = []     # Lista de puntuaciones para identificar la máxima
    max_anotadores = []     # Lista de jugadores con la puntuación máxima
    # ==================================================

    # Si no hay jugadores, avisa al usuario
    if not lista_jugadores:
        print("\nNo hay jugadores registrados aún.")
        return

    # Suma las canastas de cada jugador y determina la máxima puntuación
    for jugador in lista_jugadores:
        puntos = (int(jugador["Canastas de 3"]) * 3 + int(jugador["Canastas de 2"]) * 2
                  + int(jugador["Canastas de 1"]))
        lista_puntuaciones.append(puntos)  # Añade la puntuación total a la lista

    max_puntuacion = max(lista_puntuaciones)  # Obtiene la máxima puntuación

    for jugador in lista_jugadores:
        puntos = (int(jugador["Canastas de 3"]) * 3 + int(jugador["Canastas de 2"]) * 2
                  + int(jugador["Canastas de 1"]))

        if puntos == max_puntuacion:
            max_anotadores.append(jugador["Nombre"])

    # Resultado según cantidad de máximos anotadores
    if len(max_anotadores) == 1:
        print(f"El máximo anotador es: {max_anotadores[0]} con {max_puntuacion} puntos.")
    else:
        print("Los máximos anotadores son:")
        for nombre in max_anotadores:
            print(f"- {nombre}")
        print(f"Cada uno con {max_puntuacion} puntos.")


# PROGRAMA -----------------------------------------------------------------------------------------

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

        # inicializa opción 1  -----
        if opcion == "1":
            agregar_jugador(listado_jugadores)  # llama a la función de añadir jugadores

        # inicializa opción 2   -----
        elif opcion == "2":
            listar_jugadores(listado_jugadores)  # llama a la función de listar jugadores

        # inicializa opción 3   -----
        elif opcion == "3":
            maximo_anotador(listado_jugadores)  # llama a la función de máximo anotador

        # inicializa opción 4  -----
        elif opcion == "4":
            pass

        # Sle del programa
        elif opcion == "0":
            print("¡Gracias por usar la aplicación! Hasta pronto.")
            break

        # en caso de valor invalido para opción elegida, se avisa al usuario
        else:
            print("Opción no válida, por favor intente de nuevo.")
    else:
        print("Entrada inválida. Responda 'Si' o 'No'.")
        decision = saludo()  # Re-pregunta si la entrada inicial fue inválida
