import librerias
import pestanas

class PestanaAyuda(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana)
        self.etiqueta = self.crear_label("Ayuda")
        self.etiqueta.pack(padx=10, pady=10)
        self.etiqueta.config(font=("Arial", 20))
        
        self.crear_grafico = self.crear_boton("¿Como creo un gráfico?", self.crear_graficos)
    
    
    def crear_graficos(self):
        """Función que se ejecuta al pulsar el botón"""
        messagebox.showinfo("Información", "Para crear un gráfico, selecciona los datos y pulsa el botón 'Crear gráfico'")