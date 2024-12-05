# LIBRERÍA PARA LA GESTIÓN DE UN CLUB DE BASKET

# Clase Jugador

"""ATRIBUTOS
- nombre (str)
- edad (int)
- altura (cm) (int)
- peso (kg) (int)
- dorsal
"""

"""Metodos
- print_jugador"""

class Jugador():
    
    def __init__(self, nombre="", edad = 18, altura = 180, dorsal=0, peso=75):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal
        self.peso = peso
    
    
    def print_jugador(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")
        print(f"Dorsal: {self.dorsal}")
        
        