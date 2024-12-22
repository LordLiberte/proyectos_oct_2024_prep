"""Aquí se crea la clase Ventana Principal y se adicionan las pestañas necesarias para el funcionamiento del programa"""

from librerias import *
from Pestanas import *

class VentanaPrincipal:
    
    # Atributos de clase
    def __init__(self):
        self.ventana = tk.Tk()  # Inicializa la ventana principal
        self.ventana.title("ManagerPy") # Título de la ventana
        self.ventana.geometry("1280x720") # Tamaño de la ventana
        self.ventana.resizable(0, 0) # No se puede redimensionar la ventana
        
        self.crear_pestanas() # Crea las pestañas
    
    # Métodos de clase
    def crear_pestanas(self):
        # Crear pestañas
        self.pestanas = ttk.Notebook(self.ventana)
        self.pestanas.pack(fill="both", expand="yes")
        
        # Pestaña de inicio
        self.pestana_inicio = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pestana_inicio, text="Inicio")
        
        # Pestaña de empleados
        self.pestana_empleados = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pestana_empleados, text="Empleados")
        
        # Pestaña de plantas
        self.pestana_plantas = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pestana_plantas, text="Plantas")
        
        # Pestaña de configuración
        self.pestana_configuracion = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pestana_configuracion, text="Configuración")
        
        # Pestaña de ayuda
        self.pestana_ayuda = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pestana_ayuda, text="Ayuda")
        
    
    # Bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()
    