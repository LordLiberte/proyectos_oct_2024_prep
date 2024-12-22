"""Aqui se definen las caracteristicas y widgets de la pestaña plantas"""

from librerias import * # Importa las librerías necesarias
import Pestanas.pestanas as pestanas


archivo = "Portfolio\\Actividad_2_POO\\directorio_json\\db_secciones.json"

class PestanaFunciones(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana) # Hereda los atributos de la clase padre
        self.etiqueta = self.crear_label("Gestión de Secciones", x=480, y=10, width=320, height=50) # Crea una etiqueta en la pestaña
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center") # Configura la fuente de la etiqueta
        self.crear_widgets()
        
        # Privadas
        self.__label = ""
        
        # Genera las entradas directamente con la pestaña
        self.__seccion = self.crear_entry(x=200, y=120, width=400, height=30)
        self.__funciones = self.__funciones = self.crear_entry(x=200, y=200, width=400, height=30)
        self.__nombre_funcion = self.__nombre_funcion = self.crear_entry(x=200, y=160, width=400, height=30)
        
        # Verficador de campos llenos
        self.__verificar_parametros = False
        
        # arranques con pestaña
        self.visualizar_info()
        

    # Métodos de clase ============================================================================================================
    
    # Crea etiquetas y botones ====================================================================================================
    def crear_widgets(self):
        
        # Sección empresa ==========================================================================================================
        self.__label = self.crear_label("Sección", x=50, y=115, width=60, height=40) # Crea una etiqueta en la pestaña
        
        # Nombre de la función =====================================================================================================
        self.__label = self.crear_label("Función", x=50, y=195, width=120, height=40)
        
        # Funciones ===============================================================================================================
        self.__label = self.crear_label("Nombre de la función", x=50, y=155, width=160, height=40)
        
        # Etiqueta guardar ========================================================================================================
        self.__label = self.crear_label("Guardar/Eliminar información", x=70, y=70, width=300, height=30)
        self.__label.config(font=("Arial", 15), anchor="center", justify="center")
        
        
        # BOTONERIA
        self.boton_guardar = self.crear_boton("Guardar", funcion=self.guardar_info, x=50, y=260, width=100, height=30)
        self.boton_eliminar = self.crear_boton("Eliminar", funcion=self.eliminar_info, x=200, y=260, width=100, height=30)
        self.visualizar = self.crear_boton("Actualizar Tabla", funcion=self.visualizar_info, x=350, y=260, width=150, height=30)
        
    
    # Agrega información al JSON ================================================================================================
    def guardar_info(self):
        
        # Comprueba que todos los campos esten llenos
        try:
            if self.__funciones.get() != "" and self.__nombre_funcion.get() != "" and self.__seccion.get() != "":
                self.__verificar_parametros = True
                if self.__verificar_parametros:
                    datos = {"Seccion": self.__seccion.get(),
                            "Nombre de la función": self.__nombre_funcion.get(),
                            "Funciones": self.__funciones.get()} # Guarda los datos en un diccionario
                    
                    # Cargar datos existentes si el archivo ya existe
                    datos_existentes = []
                    if os.path.exists(archivo):
                        with open(archivo, "r") as file:
                            try:
                                datos_existentes = json.load(file)
                                datos_existentes = list(datos_existentes)  # Lo convertimos a diccionario
                            except json.JSONDecodeError:
                                datos_existentes = []  # Si el archivo está vacío o corrupto, iniciamos con una lista vacía
                    
                    # Agregar el nuevo dato a la lista de datos existentes
                    with open(archivo, 'r') as file:
                        if datos not in datos_existentes:
                            datos_existentes.append(datos)
                    
                    # Guardar los datos actualizados en el archivo JSON
                    with open(archivo, "w") as file:
                        json.dump(datos_existentes, file, indent=4)
                    
                    with open(archivo, "r") as file:
                        datos_existentes = json.load(file)
                        if datos in datos_existentes:
                            messagebox.showinfo("Información", "La información ha sido guardada correctamente")
                    
            else:
                self.__verificar_parametros = False
                messagebox.showerror("Error", "Por favor, llene todos los campos")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
            
    # Elimina información del JSON ===============================================================================================
    def eliminar_info(self):
        # Comprueba que todos los campos esten llenos
        try:
            if self.__funciones.get() != "" and self.__nombre_funcion.get() != "" and self.__seccion.get() != "":
                self.__verificar_parametros = True
                if self.__verificar_parametros:
                    
                        dato_a_eliminar = {"Seccion": self.__seccion.get(),
                                "Nombre de la función": self.__nombre_funcion.get(),
                                "Funciones": self.__funciones.get()} # Guarda los datos en un diccionario
                        
                        # Verificar si el archivo existe
                        if not os.path.exists(archivo):
                            messagebox.showerror("Error", "El archivo JSON no existe")
                            return
                        
                        # Leer los datos existentes del archivo
                        try:
                            with open(archivo, "r") as file:
                                datos_existentes = json.load(file)
                        except json.JSONDecodeError:
                            messagebox.showerror("Error", "El archivo JSON está corrupto o vacío")
                            return
                        
                        # Filtrar los datos para eliminar el dato coincidente
                        datos_actualizados = [dato for dato in datos_existentes if dato != dato_a_eliminar]
                        
                        # Verificar si el dato fue eliminado
                        if len(datos_existentes) == len(datos_actualizados):
                            messagebox.showinfo("Información", "No se encontró el dato a eliminar")
                            return
                        
                        # Guardar los datos actualizados en el archivo
                        with open(archivo, "w") as file:
                            json.dump(datos_actualizados, file, indent=4)
                        
                        messagebox.showinfo("Éxito", "El dato ha sido eliminado correctamente")
                else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos antes de eliminar")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    # Muestra en una tabla la información del JSON ==============================================================================
    def visualizar_info(self):
       
       with open(archivo, "r") as file:
           datos = json.load(file)
           datos = pd.DataFrame(datos)
       
       self.tabla = self.crear_treeview(datos, x=550, y=70, width=700, height=600)
       
        

        
        
        
        
        
        