# La principal ventaja de las funciones es su reusabilidad.
# Podemos llamarla siempre que queramos psandole ciertos parametros.
# Otra ventaja es su modularidad. Consiste en crear un codigo basado en funciones que se llamen unos a otros
# Haciendo que el codigo sea más denso pero más legible y escalable

def saludo():
    print("Hola Mundo")

# función de suma
def suma(a, b):
    print(a+b)

suma(3, 5) # llamada a la función