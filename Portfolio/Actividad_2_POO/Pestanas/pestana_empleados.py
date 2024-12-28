"""Aqui se definen las caracteristicas y widgets de la pestaña empleados"""

from librerias import *
import Pestanas.pestanas as pestanas

archivo_a_leer = "Portfolio\\Actividad_2_POO\\directorio_json\\db_secciones.json"
archivo_a_escribir = "Portfolio\\Actividad_2_POO\\directorio_json\\db_empleados.json"

class PestanaEmpleados(pestanas.Pestana):
    
    def __init__(self, nombre, ventana):
        """Inicializa la pestaña de empleados y sus widgets"""
        super().__init__(nombre, ventana)
        self._inicializar_interfaz()
        self.visualizar_info()
    
    def _inicializar_interfaz(self):
        """Inicializa todos los elementos de la interfaz"""
        # Título
        self.etiqueta = self.crear_label("Gestión de Empleados", x=480, y=10, width=320, height=50)
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center")
        
        # Campos de entrada
        self.nombre = self.crear_entry(x=200, y=100, width=150, height=30)
        self.label_nombre = self.crear_label("Nombre", x=50, y=100, width=150, height=30)

        self.apellido = self.crear_entry(x=200, y=140, width=150, height=30)
        self.label_apellido = self.crear_label("Apellido", x=50, y=140, width=150, height=30)

        self.edad = self.crear_entry(x=200, y=180, width=150, height=30)
        self.label_edad = self.crear_label("Edad", x=50, y=180, width=150, height=30)

        self.num_operario = self.crear_entry(x=200, y=220, width=150, height=30)
        self.label_num_operario = self.crear_label("Nº Operario", x=50, y=220, width=150, height=30)
        self.boton_random_generate = self.crear_boton("Generar numero aleatorio", self.generar_numero, x=360, y=220, width=100, height=30)

        # Comboboxes
        self.secciones = self.crear_combobox(self.cargar_datos_secciones(), x=200, y=260, width=150, height=30)
        self.label_secciones = self.crear_label("Sección", x=50, y=260, width=150, height=30)
        # Añadir el evento de selección al combobox de secciones
        self.secciones.bind('<<ComboboxSelected>>', self.actualizar_funciones_por_seccion)

        self.nombre_funcion = self.crear_combobox([], x=200, y=300, width=150, height=30)
        self.label_nombre_funcion = self.crear_label("Nombre de la función", x=50, y=300, width=150, height=30)
        
        # Botones de acción
        self.guardar = self.crear_boton("Guardar", self.guardar_info, x=50, y=350, width=100, height=30)
        self.eliminar = self.crear_boton("Eliminar", self.eliminar_info, x=200, y=350, width=100, height=30)
        self.visualizar = self.crear_boton("Actualizar Tabla", self.visualizar_info, x=350, y=350, width=150, height=30)

    # Métodos de carga de datos
    def cargar_datos_secciones(self):
        """Carga los valores de sección del json db_secciones al combobox"""
        secciones_temp = set()
        with open(archivo_a_leer, "r") as file:
            self.datos_secciones = json.load(file)
        for value in self.datos_secciones:
            secciones_temp.add(value["Seccion"])
        return sorted(list(secciones_temp))  # Ordenamos la lista para mejor presentación
    
    def cargar_datos_nombre_funciones(self, seccion=None):
        """
        Carga los valores de nombre de función del json db_secciones al combobox
        Si se especifica una sección, solo devuelve las funciones de esa sección
        """
        self.funciones = set()
        with open(archivo_a_leer, "r") as file:
            self.datos_funciones = json.load(file)
            
        for value in self.datos_funciones:
            if seccion is None or value["Seccion"] == seccion:
                self.funciones.add(value["Nombre de la función"])
                
        return sorted(list(self.funciones))  # Ordenamos la lista para mejor presentación
    
    def actualizar_funciones_por_seccion(self, event):
        """Actualiza el combobox de funciones según la sección seleccionada"""
        seccion_seleccionada = self.secciones.get()
        
        # Limpiar el combobox de funciones
        self.nombre_funcion.set('')  # Limpia la selección actual
        
        # Obtener las funciones para la sección seleccionada
        funciones_filtradas = self.cargar_datos_nombre_funciones(seccion_seleccionada)
        
        # Actualizar los valores del combobox
        self.nombre_funcion['values'] = funciones_filtradas
        
        # Si solo hay una función disponible, seleccionarla automáticamente
        if len(funciones_filtradas) == 1:
            self.nombre_funcion.set(funciones_filtradas[0])

    # Métodos de validación
    def comprobar_campos(self):
        """Comprueba que los campos no estén vacíos"""
        self.parametros = False
        if (self.nombre.get() != "" and 
            self.apellido.get() != "" and 
            self.edad.get() != "" and 
            self.num_operario.get() != "" and 
            self.secciones.get() != "" and 
            self.nombre_funcion.get() != ""):
            self.parametros = True
        return self.parametros

    def validar_combobox(self, combobox, opciones):
        """Comprueba que los valores de los combobox no sean inventados"""
        valor_seleccionado = combobox.get()
        if valor_seleccionado not in opciones:
            messagebox.showerror("Error", f"Valor no válido en el combobox: {valor_seleccionado}. Por favor, elige un valor predefinido.")
            return False
        return True

    def verificar_numero_operario(self, numero):
        """Verifica si el número de operario ya existe en el JSON"""
        if os.path.exists(archivo_a_escribir):
            with open(archivo_a_escribir, "r") as file:
                try:
                    datos_existentes = json.load(file)
                    for empleado in datos_existentes:
                        if empleado.get("Nº Operario") == numero:
                            return True
                except json.JSONDecodeError:
                    return False
        return False

    # Métodos de gestión de datos
    def almacen_temporal_datos(self):
        """Almacena los valores de los campos rellenados"""
        self.datos_temp = {
            "Nombre": self.nombre.get(),
            "Apellido": self.apellido.get(),
            "Edad": self.edad.get(),
            "Nº Operario": self.num_operario.get(),
            "Sección": self.secciones.get(),
            "Nombre de la función": self.nombre_funcion.get()
        }
        return self.datos_temp

    def generar_numero(self):
        """Genera un número aleatorio único para el operario"""
        while True:
            numero = random.randint(1, 99999999)
            if not self.verificar_numero_operario(str(numero)):
                self.num_operario.delete(0, tk.END)
                self.num_operario.insert(0, str(numero))
                break

    # Métodos de operaciones CRUD
    def guardar_info(self):
        """Guarda la información en el json"""
        self.parametros = self.comprobar_campos()
        self.datos = self.almacen_temporal_datos()

        try:
            if self.parametros:
                # Verificar si el número de operario ya existe
                if self.verificar_numero_operario(self.num_operario.get()):
                    messagebox.showerror("Error", "El número de operario ya existe. Por favor, genera otro número.")
                    return

                # Validar los valores de los combobox
                if not self.validar_combobox(self.secciones, self.cargar_datos_secciones()):
                    return
                if not self.validar_combobox(self.nombre_funcion, self.cargar_datos_nombre_funciones()):
                    return
                
                # Cargar datos existentes si el archivo ya existe
                datos_existentes = []
                if os.path.exists(archivo_a_escribir):
                    with open(archivo_a_escribir, "r") as file:
                        try:
                            datos_existentes = json.load(file)
                            datos_existentes = list(datos_existentes)
                        except json.JSONDecodeError:
                            datos_existentes = []

                # Comprobar si los datos ya existen
                if self.datos in datos_existentes:
                    messagebox.showerror("Error", "Los datos ya existen.")
                    return
                
                # Agregar el nuevo dato a la lista de datos existentes
                datos_existentes.append(self.datos)

                # Guardar los datos actualizados en el archivo JSON
                with open(archivo_a_escribir, "w") as file:
                    json.dump(datos_existentes, file, indent=4)

                messagebox.showinfo("Información", "La información ha sido guardada correctamente")
            else:
                messagebox.showerror("Error", "Por favor, llene todos los campos")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    def eliminar_info(self):
        """Elimina la información del json"""
        self.datos_existentes = []
        self.parametros = self.comprobar_campos

        try:
            if self.parametros:
                dato_a_eliminar = self.almacen_temporal_datos()

                if not os.path.exists(archivo_a_escribir):
                    messagebox.showerror("Error", "El archivo JSON no existe")
                    return

                try:
                    with open(archivo_a_escribir, "r") as file:
                        self.datos_existentes = json.load(file)
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "El archivo JSON está corrupto o vacío")
                    return

                datos_actualizados = [dato for dato in self.datos_existentes if dato != dato_a_eliminar]

                if len(self.datos_existentes) == len(datos_actualizados):
                    messagebox.showinfo("Información", "No se encontró el dato a eliminar")
                    return

                with open(archivo_a_escribir, "w") as file:
                    json.dump(datos_actualizados, file, indent=4)

                messagebox.showinfo("Éxito", "El dato ha sido eliminado correctamente")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos antes de eliminar")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    # Métodos de visualización
    def visualizar_info(self):
        """Visualización de los datos en la tabla"""
        try:
            with open(archivo_a_escribir, "r") as file:
                datos = json.load(file)
                datos_filtrados = [persona for persona in datos if persona is not None]
        
        except json.JSONDecodeError:
            datos_filtrados = []

        datos = pd.DataFrame(datos_filtrados)
        self.tabla = self.crear_treeview(datos, x=550, y=70, width=700, height=600)
        self.tabla.bind("<ButtonRelease-1>", self.cargar_datos_fila)

    def cargar_datos_fila(self, event):
        """Carga los datos en la tabla"""
        item = self.tabla.selection()
        if item:
            valores = self.tabla.item(item, 'values')
            if valores:
                self.nombre.delete(0, tk.END)
                self.nombre.insert(0, valores[0])

                self.apellido.delete(0, tk.END)
                self.apellido.insert(0, valores[1])

                self.edad.delete(0, tk.END)
                self.edad.insert(0, valores[2])

                self.num_operario.delete(0, tk.END)
                self.num_operario.insert(0, valores[3])

                # Primero establecemos la sección
                self.secciones.set(valores[4])
                # Actualizamos las funciones disponibles para esta sección
                self.actualizar_funciones_por_seccion(None)
                # Ahora establecemos la función
                self.nombre_funcion.set(valores[5])