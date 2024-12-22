"""Aqui se definen las caracteristicas y widgets de la pestaña inicio"""

from librerias import * # Importa las librerías necesarias
import Pestanas.pestanas as pestanas

class PestanaInicio(pestanas.Pestana):
    def __init__(self, nombre, ventana):
        super().__init__(nombre, ventana)
        self.crear_widgets()
        self.etiqueta = self.crear_label("Bienvenido a ManagerPy", x=480, y=10, width=320, height=50)
        self.etiqueta.config(font=("Arial", 20))

    def crear_widgets(self):
        
        # Quienes somos ==========================================================================================================
        self.quien_somos = self.crear_label("¿Quienes somos?", x=530, y=80, width=350, height=35)
        self.quien_somos.config(font=("Arial", 15))
        
        # Descripción de "¿Quienes somos?"
        self.description = self.crear_label("Soy estudiante de la Universidad Internacional de Valencia (VIU).\nMi nombre es Carlos Gonzalez Rubio.\nEste es el proyecto para la Actividad 2 - Programación Orientada a Objetos.", 
                                            x=10, y=130, width=600, height=80)
        self.description.config(font=("Garamond", 15))
        
        # Mision ===============================================================================================================
        self.que_hacemos = self.crear_label("¿Qué hacemos?", x=10, y=250, width=280, height=35)
        self.que_hacemos.config(font=("Arial", 15))
        
        # Descripción de "¿Qué hacemos?"
        self.descripcion_que_hacemos = self.crear_label("Nos enfocamos en el desarrollo de aplicaciones que resuelvan problemas reales.\nUtilizamos metodologías ágiles para asegurar la eficiencia y calidad en nuestros proyectos.", 
                                                        x=10, y=290, width=600, height=80)
        self.descripcion_que_hacemos.config(font=("Garamond", 12))
        
        # Sobre la App ==========================================================================================================
        self.sobre_app = self.crear_label("Sobre la App", x=10, y=480, width=280, height=35)
        self.sobre_app.config(font=("Arial", 15))
        
        # Descripción de "Sobre la App"
        self.descripcion_sobre_app = self.crear_label("Esta aplicación está diseñada para gestionar diferentes aspectos de un proyecto.\nIncluye funcionalidades para la gestión de plantas, empleados y visualización de datos.", 
                                                      x=10, y=520, width=600, height=80)
        self.descripcion_sobre_app.config(font=("Garamond", 12))
    