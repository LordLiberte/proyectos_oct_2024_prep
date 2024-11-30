"""CREACIÓN DE CLASES"""

# definición de la clase
class vehiculo():
    
    # propiedades de la clase
    def __init__(self):
        color = "Azul"
    
    # método de la clase
    def acelerar(velocidad, tipo):
        print(f"Acelerando {tipo}, la velocidad es de {velocidad}km/h")

        

# Generación de objetos
coche = vehiculo.acelerar(10, "coche")

moto = vehiculo.acelerar(20, "moto")
        
        