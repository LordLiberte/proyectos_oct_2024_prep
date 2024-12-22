"""Aqui se definen las caracteristicas y widgets de la pestaña empleados"""

from librerias import *
import Pestanas.pestanas as pestanas


archivo_a_leer = "Portfolio\\Actividad_2_POO\\directorio_json\\db_secciones.json"
archivo_a_escribir = "Portfolio\\Actividad_2_POO\\directorio_json\\db_empleados.json"

class PestanaEmpleados(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        super().__init__(nombre, ventana)  # Hereda los atributos de la clase padre
        self.etiqueta = self.crear_label("Gestión de empleados", x=480, y=10, width=320, height=50)  # Crea una etiqueta en la pestaña
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center") # Configura la fuente de la etiqueta
        
        # entrys usuario y datos, privado
        # Entry y labels
        self.nombre = self.crear_entry(x=200, y=100, width=150, height=30)  # Campo de texto para Nombre
        self.label_nombre = self.crear_label("Nombre", x=50, y=100, width=150, height=30)  # Etiqueta para Nombre

        self.apellido = self.crear_entry(x=200, y=140, width=150, height=30)  # Campo de texto para Apellido
        self.label_apellido = self.crear_label("Apellido", x=50, y=140, width=150, height=30)  # Etiqueta para Apellido

        self.edad = self.crear_entry(x=200, y=180, width=150, height=30)  # Campo de texto para Edad
        self.label_edad = self.crear_label("Edad", x=50, y=180, width=150, height=30)  # Etiqueta para Edad

        self.num_operario = self.crear_entry(x=200, y=220, width=150, height=30)  # Campo de texto para Nº Operario
        self.label_num_operario = self.crear_label("Nº Operario", x=50, y=220, width=150, height=30)  # Etiqueta para Nº Operario
        self.boton_random_generate = self.crear_boton("Generar numero aleatorio", self.generar_numero, x=360, y=220, width=100, height=30)  # Botón para generar número aleatorio

        self.secciones = self.crear_combobox(self.cargar_datos_secciones(), x=200, y=260, width=150, height=30)  # Combobox para Sección
        self.label_secciones = self.crear_label("Sección", x=50, y=260, width=150, height=30)  # Etiqueta para Sección
        
        self.nombre_funcion = self.crear_combobox(self.cargar_datos_nombre_funciones(), x=200, y=300, width=150, height=30)  # Combobox para nombre funcion
        self.label_nombre_funcion = self.crear_label("Nombre de la función", x=50, y=300, width=150, height=30)  # Etiqueta para nombre funcion
        
        self.guardar = self.crear_boton("Guardar", self.guardar_info, x=50, y=350, width=100, height=30)  # Botón para guardar información
        self.eliminar = self.crear_boton("Eliminar", self.eliminar_info, x=200, y=350, width=100, height=30)  # Botón para eliminar información
        self.visualizar = self.crear_boton("Actualizar Tabla", self.visualizar_info, x=350, y=350, width=150, height=30)  # Botón para visualizar información
        
        
    # Métodos de clase
    def generar_numero(self):
        self.numero = random.randint(1, 99999999)
        self.num_operario.delete(0, tk.END)
        self.num_operario.insert(0, str(self.numero))
    
    # Almacena los valores de los entrys en un diccionario ==========================================
    def almacen_temporal_datos(self):
        self.datos_temp = {
            "Nombre": self.nombre.get(),
            "Apellido": self.apellido.get(),
            "Edad": self.edad.get(),
            "Nº Operario": self.num_operario.get(),
            "Sección": self.secciones.get(),
            "Nombre de la función": self.nombre_funcion.get()
        }
        
        return self.datos_temp

    # Comprueba que el usuario haya llenado todos los campos ========================================
    def comprobar_campos(self):
        # Comprueba que todos los campos esten llenos
        self.parametros = False
        
        if (self.nombre.get() != "" and 
                self.apellido.get() != "" and 
                    self.edad.get() != "" and 
                        self.num_operario.get() != "" and 
                            self.secciones.get() != ""):
                                self.__parametros = True
                                return self.__parametros
        else:
            return self.parametros
    
    # Guarda la información en un archivo JSON =======================================================
    def guardar_info(self):
        
        self.parametros = self.comprobar_campos()
        self.datos = self.almacen_temporal_datos()
        # Comprueba que todos los campos esten llenos
        try:
            if self.parametros:
                # Cargar datos existentes si el archivo ya existe
                datos_existentes = []
                if os.path.exists(archivo_a_escribir):
                    with open(archivo_a_escribir, "r") as file:
                        try:
                            datos_existentes = json.load(file)
                            datos_existentes = list(datos_existentes)  # Lo convertimos a diccionario
                        except json.JSONDecodeError:
                            datos_existentes = []  # Si el archivo está vacío o corrupto, iniciamos con una lista vacía
                    
                # Agregar el nuevo dato a la lista de datos existentes
                with open(archivo_a_escribir, 'w') as file:
                    if self.datos not in datos_existentes:
                        datos_existentes.append(self.datos)
                    
                # Guardar los datos actualizados en el archivo JSON
                with open(archivo_a_escribir, "w") as file:
                    json.dump(datos_existentes, file, indent=4)
                    
                with open(archivo_a_escribir, "r") as file:
                    datos_existentes = json.load(file)
                    if self.datos in datos_existentes:
                        messagebox.showinfo("Información", "La información ha sido guardada correctamente")
                    
            else:
                messagebox.showerror("Error", "Por favor, llene todos los campos")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
                
    # Elimina información del JSON ===============================================================================================
    def eliminar_info(self):
        self.datos_existentes = []
        self.parametros = self.comprobar_campos
        
        try:
            if self.parametros:
                    
                dato_a_eliminar = self.almacen_temporal_datos()
                        
                   # Verificar si el archivo existe
                if not os.path.exists(archivo_a_escribir):
                    messagebox.showerror("Error", "El archivo JSON no existe")
                    return
                        
                # Leer los datos existentes del archivo
                try:
                    with open(archivo_a_escribir, "r") as file:
                        self.datos_existentes = json.load(file)
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "El archivo JSON está corrupto o vacío")
                    return
                        
                # Filtrar los datos para eliminar el dato coincidente
                datos_actualizados = [dato for dato in self.datos_existentes if dato != dato_a_eliminar]
                        
                # Verificar si el dato fue eliminado
                if len(self.datos_existentes) == len(datos_actualizados):
                    messagebox.showinfo("Información", "No se encontró el dato a eliminar")
                    return
                        
                # Guardar los datos actualizados en el archivo
                with open(archivo_a_escribir, "w") as file:
                    json.dump(datos_actualizados, file, indent=4)
                        
                    messagebox.showinfo("Éxito", "El dato ha sido eliminado correctamente")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos antes de eliminar")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    
    
    # Carga los datos de la pestaña de secciones para el combobox ========================================
    def cargar_datos_secciones(self):
        
        self.secciones = []
        
        with open(archivo_a_leer, "r") as file:
            self.datos_secciones = json.load(file)
        
        for value in self.datos_secciones:
            self.secciones.append(value["Seccion"])
            
        return self.secciones
    
    # Carga los datos de la pestaña de funciones para el combobox ========================================
    def cargar_datos_nombre_funciones(self):
        
        self.funciones = []
        
        with open(archivo_a_leer, "r") as file:
            self.datos_funciones = json.load(file)
        
        for value in self.datos_funciones:
            self.funciones.append(value["Nombre de la funci\u00f3n"])
            
        return self.funciones
    
    # Carga los datos de la fila seleccionada del Treeview en los campos de entrada ==========================
    def cargar_datos_fila(self, event):
        item = self.tabla.selection()
        if item:
            valores = self.tabla.item(item, 'values')
            if valores:
                # Asignar valores a los campos correspondientes
                self.nombre.delete(0, tk.END)
                self.nombre.insert(0, valores[0])  # Nombre

                self.apellido.delete(0, tk.END)
                self.apellido.insert(0, valores[1])  # Apellido

                self.edad.delete(0, tk.END)
                self.edad.insert(0, valores[2])  # Edad

                self.num_operario.delete(0, tk.END)
                self.num_operario.insert(0, valores[3])  # Nº Operario

                self.secciones.set(valores[4])  # Sección
                self.nombre_funcion.set(valores[5])  # Nombre de la función
    
    
    # Muestra en una tabla la información del JSON ==============================================================================
    def visualizar_info(self):
        with open(archivo_a_escribir, "r") as file:
            datos = json.load(file)
            datos = pd.DataFrame(datos)

        self.tabla = self.crear_treeview(datos, x=550, y=70, width=700, height=600)

        # Conectar el evento al método
        self.tabla.bind("<ButtonRelease-1>", self.cargar_datos_fila)