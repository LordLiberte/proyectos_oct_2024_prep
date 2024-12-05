import pygame

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
    
    def mover_arriba(self, y=-5):
        self.__rect.move_ip(0, y)
    
    def mover_abajo(self, y=5):
        self.__rect.move_ip(0, y)
        
    def mover_derecha(self, x=5):
        self.__rect.move_ip(x, 0)
    
    def mover_izquierda(self, x=-5):
        self.__rect.move_ip(x, 0)
    
    def get_imagen(self):
        return self.__img
    
    def get_rect(self):
        return self.__rect