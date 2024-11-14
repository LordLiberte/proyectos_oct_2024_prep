# funciona más o menos pero pa que más, en caso de necesitar que funcione OK -> REVISAR

import random
import string
from itertools import chain


# Función para generar pasword
def pass_generation(long, caracteres):
    passw = ""
    for v in range(0, long):
        valor = random.choice(caracteres)
        passw += valor

    print(passw)

# Longitud password

# Elementos que utilizaremos para construir password
print("Elige entre los siguientes subgrupos")
print("1. Digitos")
print("2. Minusculas")
print("3. Mayusculas")
print("4. Caracteres especiales")
print("5. q para salir")

listaCaracteres = ""
# Bucle donde se solicita caracteres a usar
while True:
    lenght = int(input("Introduce la longitud del password: "))
    while True:
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            numeros = string.digits
            listaCaracteres += numeros

        if opcion == 2:
            letras_min = string.ascii_lowercase
            listaCaracteres += letras_min

        if opcion == 3:
            letras_may = string.ascii_uppercase
            listaCaracteres += letras_may

        if opcion == 4:
            car_especiales = string.punctuation
            listaCaracteres += car_especiales

        pass_generation(lenght, listaCaracteres)


