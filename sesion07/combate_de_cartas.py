"""Pequeño juego de combates de cartas entre jugadores"""

class Carta:
    
    # Definimos caracteristicas iniciales de la carta creada
    def __init__(self, nombre, tipo, ptos_ataque, ptos_defensa, quitar_vida):
        self.nombre = ""
        self.tipo = ""
        self.ptos_ataque = 0
        self.ptos_defensa = 0
        self.quitar_vida = 0
    
    
    def ataque(self):
        print(f"Atacando con {self.ptos_ataque} puntos de ataque!")
    
    def defensa(self):
        print(f"Defendiendo con {self.ptos_defensa} puntos de defensa!")


carta1 = Carta("Magicarp", "Agua", 200, 450, 1)
carta2 = Carta("Doraemon", "Mágico", 350, 100, 1)

lista_cartas = []


if carta1.ataque < carta2.defensa:
    print("El ataque es menor que la defensa, la carta es eliminada")
    lista_cartas.pop()
