"""Aqui se definen las caracteristicas y widgets de la pestaña inicio"""

from librerias import * # Importa las librerías necesarias
import Pestanas.pestanas as pestanas

class PestanaInicio(pestanas.Pestana):
    def __init__(self, nombre, ventana):
        super().__init__(nombre, ventana)
        self.crear_widgets()
        self.etiqueta = self.crear_label("Bienvenido a ManagerPy", x=480, y=10, width=320, height=50)
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center")

    def crear_widgets(self):
        
        # Ancho de la ventana
        ventana_ancho = 1280
        
    
        # Quienes somos ==========================================================================================================
        self.quien_somos = self.crear_label("¿Quienes somos?", x=(ventana_ancho - 350) // 2, y=80, width=350, height=35)
        self.quien_somos.config(font=("Arial", 15), anchor="center", justify="center")
        
        # Descripción de "¿Quienes somos?" --------------------------------------------------------------------------------------
        self.description = self.crear_label("Soy estudiante de la Universidad Internacional de Valencia (VIU).\nMi nombre es Carlos Gonzalez Rubio.\nEste es el proyecto para la Actividad 2 - Programación Orientada a Objetos.", 
                                            x=(ventana_ancho -700) // 2, y=120, width=700, height=80)
        self.description.config(font=("Garamond", 15), anchor="center", justify="center")
        
        
        
        # Mision ===============================================================================================================
        self.que_hacemos = self.crear_label("¿Qué hacemos?", x=(ventana_ancho - 280) // 2, y=250, width=280, height=35)
        self.que_hacemos.config(font=("Arial", 15), anchor="center", justify="center")
        
        # Descripción de "¿Qué hacemos?" ----------------------------------------------------------------------------------------
        self.descripcion_que_hacemos = self.crear_label("Nos enfocamos en el desarrollo de aplicaciones que resuelvan problemas reales.\nUtilizamos metodologías ágiles para asegurar la eficiencia y calidad en nuestros proyectos.", 
                                                        x=(ventana_ancho -700) // 2, y=280, width=700, height=80)
        self.descripcion_que_hacemos.config(font=("Garamond", 15), anchor="center", justify="center")
        
        
        
        # Sobre la App ==========================================================================================================
        self.sobre_app = self.crear_label("Sobre la App", x=(ventana_ancho - 300) // 2, y=380, width=300, height=35)
        self.sobre_app.config(font=("Arial", 15), anchor="center", justify="center")
        
        # Descripción de "Sobre la App" ------------------------------------------------------------------------------------------
        self.descripcion_sobre_app = self.crear_label("Esta aplicación está diseñada para gestionar diferentes aspectos de un proyecto.\nIncluye funcionalidades para la gestión de plantas, empleados y visualización de datos.", 
                                                      x=(ventana_ancho -700) // 2, y=410, width=700, height=80)
        self.descripcion_sobre_app.config(font=("Garamond", 15), anchor="center", justify="center")
    