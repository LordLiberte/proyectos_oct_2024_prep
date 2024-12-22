"""Aqui se definen las caracteristicas y widgets de la pestaña visualización"""

from librerias import *
import Pestanas.pestanas as pestanas

class PestanaVisualizacion(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana) # Hereda los atributos de la clase padre
        self.etiqueta = self.crear_label("Configuración", 10, 10, 100, 100) # Crea una etiqueta en la pestaña
        self.etiqueta.config(font=("Arial", 20)) # Configura la fuente de la etiqueta