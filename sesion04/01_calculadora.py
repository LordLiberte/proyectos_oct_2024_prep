# MOSTRAR LAS FUNCIONES AL USUARIO
def inicio_calculadora():
    operaciones = ["Suma", "Resta", "Multiplicar", "Dividir", "Salir"]
    indice = 1
    indice_operaciones = 0
    print("¿Que desea realizar?")

    for elemento in operaciones:
        print(f"{indice}. {operaciones[indice_operaciones]}")
        indice += 1
        indice_operaciones +=1

# ELECCION DE OPERACIÓN DEL USUARIO
    eleccion = input("Seleccione acción [1,2,3,4,5] ")
    eleccion = int(eleccion)
    return eleccion

# OPERACIONES
def suma(a, b):
    print(a+b)

def resta(a,b):
    print(a-b)

def multiplicar(a,b):
    print(a*b)

def division(a, b):
    print(a/b)

# ELECCION DE VALORES
def definir_valores():
    valor_a = input("Valor 1: ")
    valor_b = input("Valor 2: ")
    valor_a = int(valor_a)
    valor_b = int(valor_b)
    return valor_a, valor_b  # en su llamada deberemos poner los valores en este orden


while True:

    eleccion = inicio_calculadora()

    if eleccion == 5:
        print("Gracias por venir!")
        break

    # DEFINIMOS LOS VALORES DE LAS VARIABLES A OPERAR
    a, b = definir_valores()

    # ACCIONES A REALIZAR EN FUNCIÓN DE USUARIO INPUT
    if eleccion == 1:
        suma(a, b)
    elif eleccion == 2:
        resta(a, b)
    elif eleccion == 3:
        multiplicar(a, b)
    else:
        division(a, b)

