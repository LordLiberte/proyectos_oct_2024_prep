"""Aqui se definen las caracteristicas y widgets de la pestaña ayuda"""

from librerias import *
import Pestanas.pestanas as pestanas

class PestanaAyuda(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana)
        self.etiqueta = self.crear_label("Ayuda", x=480, y=10, width=320, height=50)
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center")