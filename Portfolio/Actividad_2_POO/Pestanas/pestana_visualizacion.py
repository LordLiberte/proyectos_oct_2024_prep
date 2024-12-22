import librerias
import pestanas

class PestanaVisualizacion(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana) # Hereda los atributos de la clase padre
        self.etiqueta = self.crear_label("Configuración") # Crea una etiqueta en la pestaña
        self.etiqueta.pack(padx=10, pady=10) # Empaqueta la etiqueta
        self.etiqueta.config(font=("Arial", 20)) # Configura la fuente de la etiqueta