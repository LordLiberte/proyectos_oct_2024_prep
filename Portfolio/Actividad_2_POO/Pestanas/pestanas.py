"""Aquí se crean los widgets, configuraciones, etc. Que se usarán en las pestañas de la aplicación"""

# Importa las librerías necesarias
from librerias import *

# Clase padre
class Pestana:
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        self.nombre = nombre # Nombre de la pestaña
        self.ventana = ventana # Ventana principal
        self.pestana = tk.Frame(self.ventana) # Crea una pestaña en la ventana
        self.ventana.add(self.pestana, text=self.nombre) # Añade la pestaña a la ventana
        self.ventana.pack(expand=1, fill='both') # Empaqueta la ventana
        
    # Métodos de clase
    # BOTÓN @@@@@
    def crear_boton(self, nombre, funcion, x, y, width, height):
        """Crea un botón en la pestaña"""
        self.x = x # Posición en x
        self.y = y # Posición en y
        self.width = width # Ancho
        self.height = height # Alto
        
        boton = ttk.Button(self.pestana, text=nombre, command=funcion) # Crea un botón en la pestaña
        boton.place(x=self.x, y=self.y, width=self.width, height=self.height) # Ubica el botón en la pestaña donde se le indique
        boton.config(cursor="hand2") # Cambia el cursor al pasar por encima del botón
        return boton

    # DEPLEGABLE @@@@@
    def crear_combobox(self, valores, x, y, width, height):
        """Crea un combobox en la pestaña"""
        self.x = x # Posición en x
        self.y = y # Posición en y
        self.width = width # Ancho
        self.height = height # Alto
        
        combobox = ttk.Combobox(self.pestana, values=valores) # Crea un combobox en la pestaña
        combobox.place(x=self.x, y=self.y, width=self.width, height=self.height) # Ubica el combobox en la pestaña donde se le indique
        return combobox
    
    # ENTRADA DE TEXTO @@@@@
    def crear_entry(self, x, y, width, height):
        """Crea un entry en la pestaña"""
        self.x = x # Posición en x
        self.y = y # Posición
        self.width = width # Ancho
        self.height = height # Alto
        
        entry = ttk.Entry(self.pestana) # Crea un entry en la pestaña
        entry.place(x=self.x, y=self.y, width=self.width, height=self.height) # Ubica el entry en la pestaña donde se le indique
        return entry

    # ETIQUETA @@@@@
    def crear_label(self, texto, x, y, width, height):
        """Crea una etiqueta en la pestaña"""
        self.x = x # Posición en x
        self.y = y # Posición en y
        self.width = width  # Ancho
        self.height = height # Alto
        
        label = ttk.Label(self.pestana, text=texto) # Crea una etiqueta en la pestaña
        label.place(x=self.x, y=self.y, width=self.width, height=self.height) # Ubica la etiqueta en la pestaña donde se le indique
        return label
    
    # Crear el Treeview y almacenarlo en self.tabla
    def crear_treeview(self, informacion, x, y, width, height):
        """Crea un Treeview en la pestaña"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Verifica que la informacion sea un DataFrame de pandas
        if not isinstance(informacion, pd.DataFrame):
            raise ValueError("La informacion debe ser un DataFrame de pandas")

        # Crear el Treeview
        treeview = ttk.Treeview(self.pestana, columns=list(informacion.columns), show="headings")
        treeview.place(x=self.x, y=self.y, width=self.width, height=self.height)

        # Configurar encabezados de las columnas
        for col in informacion.columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=100, anchor="center")

        # Insertar datos en el Treeview
        for index, row in informacion.iterrows():
            treeview.insert("", "end", values=list(row))

        # Almacenar la referencia del Treeview en self.tabla
        self.tabla = treeview

        return treeview
        
        
