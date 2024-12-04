from enum import Enum


class Colores(Enum):
    ROJO = 1
    AMARILLO = 2
    VERDE = 3


semaforo = Colores.AMARILLO 
print(semaforo)
semaforo = Colores.AMARILLO.name  # Accede al nombre de la varaible dentro de la clase
print(semaforo)
semaforo = Colores.AMARILLO.value # Accede al valor de la variable con tal nombre
print(semaforo)