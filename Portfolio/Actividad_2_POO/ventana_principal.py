"""Aquí se crea la clase Ventana Principal y se adicionan las pestañas necesarias para el funcionamiento del programa"""

from librerias import * # Importa las librerías necesarias
import Pestanas.pestanas as pestanas # Importa las pestañas necesarias
import Pestanas.pestana_inicio as p_inicio


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
        p_inicio("Inicio", self.pestanas) # Envia la información de la pestaña
        
        # Pestaña de empleados
        pestanas.PestanaEmpleados("Empleados", self.pestanas)
        
        # Pestaña de plantas
        pestanas.PestanaPlantas("Plantas", self.pestanas)
        
        # Pestaña de Visualización
        pestanas.PestanaVisualizacion("Configuración", self.pestanas)
        
        # Pestaña de ayuda
        pestanas.PestanaAyuda("Ayuda", self.pestanas)
        
    
    # Bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop() 
    