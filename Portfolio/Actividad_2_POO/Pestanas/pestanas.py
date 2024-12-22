"""Aquí se crean las pestañas de la aplicación"""

# Importa las librerías necesarias
from librerias import *
import pestana_inicio

# Clase padre
class Pestana:
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        self.nombre = nombre # Nombre de la pestaña
        self.ventana = ventana # Ventana principal
        self.pestana = ttk.Frame(self.ventana) # Crea una pestaña en la ventana
        self.ventana.add(self.pestana, text=self.nombre) # Añade la pestaña a la ventana
        self.ventana.pack(expand=1, fill='both') # Empaqueta la ventana
        
    # Métodos de clase
    def crear_boton(self, nombre, funcion, x, y, widht, height):
        """Crea un botón en la pestaña"""
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
        boton = ttk.Button(self.pestana, text=nombre, command=funcion) # Crea un botón en la pestaña
        boton.place(x=self.x, y=self.y, widht=self.widht, height=self.height) # Ubica el botón en la pestaña donde se le indique
        return boton

    def crear_combobox(self, valores, x, y, widht, height):
        """Crea un combobox en la pestaña"""
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
        combobox = ttk.Combobox(self.pestana, values=valores) # Crea un combobox en la pestaña
        combobox.place(x=self.x, y=self.y, widht=self.widht, height=self.height) # Ubica el combobox en la pestaña donde se le indique
        return combobox
    
    def crear_entry(self, x, y, widht, height):
        """Crea un entry en la pestaña"""
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
        entry = ttk.Entry(self.pestana) # Crea un entry en la pestaña
        entry.place(x=self.x, y=self.y, widht=self.widht, height=self.height) # Ubica el entry en la pestaña donde se le indique
        return entry

    def crear_label(self, texto, x, y, widht, height):
        """Crea una etiqueta en la pestaña"""
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
        label = ttk.Label(self.pestana, text=texto) # Crea una etiqueta en la pestaña
        label.place(x=self.x, y=self.y, widht=self.widht, height=self.height) # Ubica la etiqueta en la pestaña donde se le indique
        return label
            
