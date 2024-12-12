import pygame
from enum import Enum

# Clase GameObject

class GameObject:
    
    def __init__(self, tag, pox=0, poy=0, image="individual.png"):
        print(f"Creando el GameObject {tag}")
        
        # Atributos de instancia
        self.tag = tag
        self.pox = pox
        self.poy = pox
        self.image = image
        
        # Atributo privado
        self.__img = pygame.image.load(self.image)
        self.__img.convert()
        self.__rect = self.__img.get_rect()
        self.__rect.center = pox, poy
    
    def mover_arriba(self, y=-1):
        self.__rect.move_ip(0, y)
    
    def mover_abajo(self, y=1):
        self.__rect.move_ip(0, y)
     
    def mover_derecha(self, x=1):
        self.__rect.move_ip(x, 0)
    
    def mover_izquierda(self, x=-1):
        self.__rect.move_ip(x, 0)
    
    def get_imagen(self):
        return self.__img
    
    def get_rect(self):
        return self.__rect
    
    
    
# HIJOS
class Personaje(GameObject):
    
    def __init__(self, tag, pox=0, poy=0, image="individual.png",  life=3):
        super().__init__(tag, pox, poy, image)
        self.life = life
    
    def quitar_vida(self, danyo=1):
        self.life -= danyo
        print(f"Ahora tienes {self.life} vidas")
        

class TypeObstacle(Enum):
    FURNITURE = 0
    TRAP = 1
    
class Damage(Enum):
    LIGHT = 0
    HEAVY = 1

class Obstaculo(GameObject):
    
    def __init__(self, tag, pox=0, poy=0, image="individual.png", typeobstacle=TypeObstacle.FURNITURE):
        super().__init__(tag, pox, poy, image)
        self.typeobstacle
        
        # self.__hurt = 0 if typeobstacle == TypeObstacle.FURNITURE else 1  -> condicional ternario
        
        if typeobstacle == TypeObstacle.TRAP:
            self.__damage = Damage.HEAVY
        else:
            self.__damage = Damage.LIGHT
        
        