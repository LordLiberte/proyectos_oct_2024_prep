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

from librerias import *

# Configuración del sistema de logging
def configurar_logging():
    """Configura el sistema de logging para la aplicación"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    log_filename = f'logs/managerpy_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

class ErrorAplicacion(Exception):
    """Clase base para excepciones personalizadas de la aplicación"""
    pass

class ErrorImportacion(ErrorAplicacion):
    """Error al importar módulos"""
    pass

class ErrorInicializacion(ErrorAplicacion):
    """Error al inicializar componentes"""
    pass

class VentanaPrincipal:
    def __init__(self):
        """Inicializa la ventana principal con manejo de errores"""
        try:
            self._importar_modulos()
            self._inicializar_ventana()
            self._crear_pestanas()
            logging.info("Aplicación iniciada correctamente")
        except Exception as e:
            self._manejar_error_inicializacion(e)
    
    def _importar_modulos(self):
        """Importa los módulos necesarios con manejo de errores"""
        try:
            # Intentamos importar todos los módulos necesarios
            import Pestanas.pestana_inicio as pestana_inicio
            import Pestanas.pestana_funciones as pestana_funciones
            import Pestanas.pestana_empleados as pestanas_empleados
            import Pestanas.pestana_visualizacion as pestanas_visualizacion
            import Pestanas.pestana_ayuda as pestanas_ayuda
            
            # Guardamos las referencias a los módulos
            self.modulos = {
                'inicio': pestana_inicio,
                'funciones': pestana_funciones,
                'empleados': pestanas_empleados,
                'visualizacion': pestanas_visualizacion,
                'ayuda': pestanas_ayuda
            }
            logging.info("Módulos importados correctamente")
        except ImportError as e:
            mensaje = f"Error al importar módulos: {str(e)}"
            logging.error(mensaje)
            raise ErrorImportacion(mensaje)

    def _inicializar_ventana(self):
        """Inicializa la ventana principal con manejo de errores"""
        try:
            self.ventana = tk.Tk()
            self.ventana.title("ManagerPy")
            self.ventana.geometry("1280x720")
            self.ventana.resizable(0, 0)
            
            # Configurar protocolo de cierre
            self.ventana.protocol("WM_DELETE_WINDOW", self._confirmar_salida)
            
            logging.info("Ventana principal inicializada correctamente")
        except Exception as e:
            mensaje = f"Error al inicializar la ventana principal: {str(e)}"
            logging.error(mensaje)
            raise ErrorInicializacion(mensaje)

    def _crear_pestanas(self):
        """Crea las pestañas con manejo de errores"""
        try:
            self.pestanas = ttk.Notebook(self.ventana)
            self.pestanas.pack(fill="both", expand="yes")
            
            # Diccionario de pestañas y sus clases correspondientes
            pestanas_config = {
                'Inicio': self.modulos['inicio'].PestanaInicio,
                'Empleados': self.modulos['empleados'].PestanaEmpleados,
                'Secciones': self.modulos['funciones'].PestanaFunciones,
                'Visualización': self.modulos['visualizacion'].PestanaVisualizacion,
                'Ayuda': self.modulos['ayuda'].PestanaAyuda
            }
            
            # Crear cada pestaña con manejo de errores individual
            for nombre, clase in pestanas_config.items():
                try:
                    clase(nombre, self.pestanas)
                    logging.info(f"Pestaña '{nombre}' creada correctamente")
                except Exception as e:
                    mensaje = f"Error al crear la pestaña '{nombre}': {str(e)}"
                    logging.error(mensaje)
                    messagebox.showwarning("Error en pestaña", 
                                         f"La pestaña '{nombre}' no se pudo cargar correctamente.\n"
                                         "Algunas funcionalidades podrían no estar disponibles.")
            
        except Exception as e:
            mensaje = f"Error al crear el sistema de pestañas: {str(e)}"
            logging.error(mensaje)
            raise ErrorInicializacion(mensaje)

    def _manejar_error_inicializacion(self, error):
        """Maneja los errores durante la inicialización"""
        mensaje_error = f"Error crítico durante la inicialización: {str(error)}"
        logging.critical(mensaje_error)
        logging.critical(traceback.format_exc())
        
        messagebox.showerror("Error crítico",
                            "Ha ocurrido un error crítico al iniciar la aplicación.\n"
                            "Por favor, revise el archivo de log para más detalles.")
        sys.exit(1)

    def _confirmar_salida(self):
        """Confirma si el usuario desea salir de la aplicación"""
        if messagebox.askokcancel("Confirmar salida", 
                                 "¿Está seguro de que desea salir de la aplicación?"):
            logging.info("Aplicación cerrada por el usuario")
            self.ventana.destroy()

    def iniciar(self):
        """Inicia el bucle principal de la aplicación con manejo de errores"""
        try:
            self.ventana.mainloop()
        except Exception as e:
            logging.critical(f"Error en el bucle principal: {str(e)}")
            logging.critical(traceback.format_exc())
            messagebox.showerror("Error crítico", 
                                "Ha ocurrido un error crítico en la aplicación.\n"
                                "La aplicación se cerrará.")
            sys.exit(1)

def main():
    """Función principal con manejo de errores"""
    try:
        configurar_logging()
        app = VentanaPrincipal()
        app.iniciar()
    except Exception as e:
        logging.critical(f"Error fatal en la aplicación: {str(e)}")
        logging.critical(traceback.format_exc())
        messagebox.showerror("Error fatal",
                            "Ha ocurrido un error fatal al iniciar la aplicación.\n"
                            "Por favor, contacte con el administrador del sistema.")
        sys.exit(1)

if __name__ == "__main__":
    main()