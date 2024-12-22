"""Aqui se definen las caracteristicas y widgets de la pestaña inicio"""

from librerias import * # Importa las librerías necesarias
import pestanas

class PestanaInicio(pestanas.Pestana):
    
    # Atributos de clase ==========================================================================================================
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana)
        self.etiqueta = self.crear_label("Bienvenido a ManagerPy")
        self.etiqueta.pack(padx=10, pady=10)
        self.etiqueta.config(font=("Arial", 20))
        
        self.disenador = self.crear_boton("Diseñador", self.saludar)  # Crea un botón en la pestaña
        self.opciones = self.crear_boton("Opciones", self.opciones)  # Crea un botón en la pestaña

    # Metodos de clase ===========================================================================================================
    def saludar(self):
        """Función que se ejecuta al pulsar el botón"""
        messagebox.showinfo("Información", "Diseñado por Carlos Gonzalez Rubio") # Muestra un mensaje en pantalla
    
    def opciones(self): 
        """Función que se ejecuta al pulsar el botón"""
        messagebox.showinfo("Información", "Opciones de la aplicación") # Muestra un mensaje en pantalla