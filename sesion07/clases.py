"""Creación de clases"""

# Defincición de la clase
class Perro:
    
    # propiedades de la clase
    # init es un método especial de las clases
    def __init__(self, raza, nombre):
        print(f"Creando perro {nombre}, {raza}")
        
        # Atributos de instancia
        self.raza = raza
        self.nombre = nombre
    

# Instanciación de la clase -> Crear objetos
caniche = Perro("Caniche", "Zeus")
pastorAleman = Perro("Pastor Alemán", "Odin")
chiuaua = Perro("Chiuaua", "Loki")