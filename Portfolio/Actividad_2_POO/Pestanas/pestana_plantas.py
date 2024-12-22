"""Aqui se definen las caracteristicas y widgets de la pestaña plantas"""

from librerias import *
import Pestanas.pestanas as pestanas

class PestanaPlantas(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana) # Hereda los atributos de la clase padre
        self.etiqueta = self.crear_label("Gestión de plantas", x=480, y=10, width=320, height=50) # Crea una etiqueta en la pestaña
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center") # Configura la fuente de la etiqueta