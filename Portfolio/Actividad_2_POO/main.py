"""
Nombre: Carlos Gonzalez Rubio
Fecha Inicio: 22/12/24
Actividad 2 - Programación Orientada a Objetos
-------------------------------------------------
Descripción: 
En esta actividad se pretende poner en práctica todos los conceptos aprendidos y trabajados sobre POO con el lenguaje de programación Python.
-------------------------------------------------
Opción elegida: 
4
----    IMPORTANTE !!!   ----
ESTE ARCHIVO INICIA LA APLICACIÓN
"""

"""Aquí se crea la clase Ventana Principal y se adicionan las pestañas necesarias para el funcionamiento del programa"""

from librerias import * # Importa las librerías necesarias
import Pestanas.pestana_inicio as pestana_inicio # Importa la pestaña de inicio
import Pestanas.pestana_funciones as pestana_funciones # Importa las pestañas de plantas
import Pestanas.pestana_empleados as pestanas_empleados # Importa las pestañas de empleados
import Pestanas.pestana_visualizacion as pestanas_visualizacion # Importa las pestañas de visualización
import Pestanas.pestana_ayuda as pestanas_ayuda # Importa las pestañas de ayuda


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
        pestana_inicio.PestanaInicio("Inicio", self.pestanas) # Envia la información a la pestaña
        
        # Pestaña de empleados
        pestanas_empleados.PestanaEmpleados("Empleados", self.pestanas) # Envia la información a la pestaña
        
        # Pestaña de plantas
        pestana_funciones.PestanaFunciones("Plantas", self.pestanas) # Envia la información a la pestaña
        
        # Pestaña de Visualización
        pestanas_visualizacion.PestanaVisualizacion("Visualización", self.pestanas) # Envia la información a la pestaña
        
        # Pestaña de ayuda
        pestanas_ayuda.PestanaAyuda("Ayuda", self.pestanas) # Envia la información a la pestaña
        
    
    # Bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop() 


# Crear una instancia de VentanaPrincipal y ejecutar la aplicación
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.iniciar()