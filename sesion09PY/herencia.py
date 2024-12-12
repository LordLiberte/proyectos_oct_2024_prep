
# Clase padre
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
        
    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass
    
    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass
    
    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo ", type(self).__name__)


# Clase hijo
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
        
class Gato(Animal):
    def moverse(self):
        print("Caminando a 4 patas")
        
class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")
    # Nuevo método
    def picar(self):
        print("Picar!")


mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)
mi_perro.hablar()
mi_vaca.hablar()
 # Guau!
 # Muuu!
mi_vaca.describeme()
mi_abeja.describeme()
# Soy un Animal del tipo Vaca
# Soy un Animal del tipo Abeja
mi_abeja.picar()
# Picar!

mi_gato = Gato('mamífero', 10)
mi_gato.moverse()