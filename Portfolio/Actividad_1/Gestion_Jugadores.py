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
               "Estadísticas del equipo",
               "Ampliación"]  # Lista de opciones del usuario

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

    # Lista de características del jugador para enviar a la función
    lista_caracteristicas = [input("Indique nombre del jugador: "),
                             input("Indique dorsal del jugador: "),
                             input("Indique canastas de 3 del jugador: "),
                             input("Indique canastas de 2 del jugador: "),
                             input("Indique canastas de 1 del jugador: ")]

    # Llamada a la función de crear jugador
    jugador = nuevo_jugador(lista_caracteristicas)

    # Añade el jugador a una lista de jugadores
    listado_jugadores.append(jugador)

    # Avisa de que se ha creado el jugador
    print("\nJugador agregado correctamente")


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
    # Si no hay jugadores, avisa al usuario
    if not listado_jugadores:
        print("\nNo hay jugadores registrados aún")
    else:
        # Imprime una cadena f-string por cada jugador con sus características
        print("\nListado de jugadores:")
        for j in listado_jugadores:
            canastas_totales = (int(j["Canastas de 3"]) + int(j["Canastas de 2"]) +
                                int(j["Canastas de 3"]))
            print(f"Nombre: {j['Nombre']}, Dorsal: {j['Dorsal']}, Canastas de 3: {j['Canastas de 3']}, "
                  f"Canastas de 2: {j['Canastas de 2']}, Canastas de 1: {j['Canastas de 1']},"
                  f" Canastas totales: {canastas_totales}")


# ===================================================================
# OPCIÓN 3. Máximo anotador
# ===================================================================
def maximo_anotador(lista_jugadores):
    # Variables generales función =======================
    max_canastas = 0        # Número máximo de canastas
    max_anotadores = []     # Lista de jugadores con la puntuación máxima
    # ==================================================

    # Si no hay jugadores, avisa al usuario
    if not lista_jugadores:
        print("\nNo hay jugadores registrados aún")
        return

    # Determina el número máximo de canastas realizadas
    for jugador in lista_jugadores:
        total_canastas = (int(jugador["Canastas de 3"]) + int(jugador["Canastas de 2"]) + int(jugador["Canastas de 1"]))
        if total_canastas > max_canastas:
            max_canastas = total_canastas

    # Encuentra los jugadores con el número máximo de canastas
    for jugador in lista_jugadores:
        total_canastas = (int(jugador["Canastas de 3"]) + int(jugador["Canastas de 2"]) + int(jugador["Canastas de 1"]))
        if total_canastas == max_canastas:
            max_anotadores.append(jugador["Nombre"])

    # Resultado según cantidad de máximos anotadores
    if len(max_anotadores) == 1:
        print(f"El máximo anotador es: {max_anotadores[0]} con {max_canastas} canastas totales.")
    else:
        print("Los máximos anotadores son:")
        for nombre in max_anotadores:
            print(f"- {nombre}")
        print(f"Cada uno con {max_canastas} anotaciones")


# ===================================================================
# OPCIÓN 4. Puntuación del equipo
# ===================================================================
def puntuacion_equipo(lista_jugadores):
    # Variables generales ================================
    canastas_3 = 0
    canastas_2 = 0
    canastas_1 = 0
    canastas_totales = 0
    # ====================================================

    # Si no hay jugadores, avisa al usuario
    if not lista_jugadores:
        print("\nNo hay jugadores registrados aún.")
        return

    # Por jugador suma sus canastas
    for jugador in lista_jugadores:
        canastas_3 += int(jugador["Canastas de 3"])
        canastas_2 += int(jugador["Canastas de 2"])
        canastas_1 += int(jugador["Canastas de 1"])

    # Suma el total de canastas de todos los jugadores
    canastas_totales = (canastas_3) + (canastas_2) + canastas_1

    print("\nEstas son las estadísticas del equipo:\n")
    print(f"""
- Canastas de 3: {canastas_3},
- Canastas de 2: {canastas_2},
- Canastas de 1: {canastas_1},
- Total puntos: {canastas_totales}
""")


# =====================================================================================================================
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

        # Opción 1: Agregar jugador
        if opcion == "1":
            agregar_jugador(listado_jugadores)

        # Opción 2: Listar jugadores
        elif opcion == "2":
            listar_jugadores(listado_jugadores)

        # Opción 3: Máximo anotador
        elif opcion == "3":
            maximo_anotador(listado_jugadores)

        # Opción 4: Estadísticas del equipo
        elif opcion == "4":
            puntuacion_equipo(listado_jugadores)

        # Salir del programa
        elif opcion == "0":
            print("¡Gracias por usar la aplicación! Hasta pronto.")
            break

        # En caso de valor inválido
        else:
            print("Opción no válida, por favor intente de nuevo.")
    else:
        print("Entrada inválida. Responda 'Si' o 'No'.")
        decision = saludo()  # Re-pregunta si la entrada inicial fue inválida
