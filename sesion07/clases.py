"""Creación de clases"""

# Defincición de la clase
class Perro:
    
    # atributos de clase
    especie = "mamifero"
    habla = "guau"
    pasosTotales = 0
    
    # propiedades de la clase
    # init es un método especial de las clases
    # método constructor de caracteristicas
    def __init__(self, raza, nombre):
        print(f"Creando perro {nombre}, {raza}")
        
        # Atributos de instancia
        self.raza = raza
        self.nombre = nombre
        
    # método de acciones que puede realizar
    def ladra(self):
        print(self.habla)
    
    def caminar(self, pasos):
        
        # Debo incrementar los pasos totales
        self.pasosTotales += pasos
        print(f"Esta caminando {self.pasosTotales} pasos")
        
    

# Instanciación de la clase -> Crear objetos
caniche = Perro("Caniche", "Zeus")
pastorAleman = Perro("Pastor Alemán", "Odin")
chiuaua = Perro("Chiuaua", "Loki")

caniche.ladra()
pastorAleman.caminar(10)
pastorAleman.caminar(20)