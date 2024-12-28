"""Aqui se definen las caracteristicas y widgets de la pestaña visualización"""

from librerias import *
import Pestanas.pestanas as pestanas

archivo_empleados = "Portfolio\\Actividad_2_POO\\directorio_json\\db_empleados.json"
archivo_secciones = "Portfolio\\Actividad_2_POO\\directorio_json\\db_secciones.json"

class PestanaVisualizacion(pestanas.Pestana):
    
    # Atributos de clase
    def __init__(self, nombre, ventana):
        """Constructor de la clase"""
        super().__init__(nombre, ventana) # Hereda los atributos de la clase padre
        self.etiqueta = self.crear_label("Visualización", x=480, y=10, width=320, height=50) # Crea una etiqueta en la pestaña
        self.etiqueta.config(font=("Arial", 20), anchor="center", justify="center") # Configura la fuente de la etiqueta
        
        self.boton_visualizar_empleados = self.crear_boton("Visualizar Empleados", self.visualizar_empleados,  480, 100, 320, 50)
        
    def visualizar_empleados(self):
        
        with open(archivo_empleados, "r") as archivo:
            empleados = json.load(archivo)
            
            total_empleados = 0
            empleados_pl51 = 0
            empleados_pl55 = 0
            empleados_pl53 = 0
            dict_funciones = {"Nombre de la función": ["Encargado", "Operario", "TPM", "Operario"],
                              "Cantidad": ["", "", "", ""]}
            
            # Calcula el total de empleados y empleados por planta (2 cálculos)
            for row in empleados:
                total_empleados += 1
                if row["Sección"] == "Planta 51":
                    empleados_pl51 += 1
                elif row["Sección"] == "Planta 55":
                    empleados_pl55 += 1
                else:
                    empleados_pl53 += 1
                    
                    
            
            self.plantas = pd.DataFrame({
                "Plantas": ["Planta 51", "Planta 53", "Planta 55"],
                "Empleados": [empleados_pl51, empleados_pl53, empleados_pl55]
            })
            
            sns.barplot(x="Plantas", y="Empleados", data=self.plantas,
                        palette="viridis")
            plt.show()
            
            messagebox.showinfo("Visualización de Empleados", f"El total de empleados es: {total_empleados}")
            
            


            