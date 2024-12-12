class Persona:
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):  # comprueba que sea una cadena 
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:  # comprueba que sea integer y sea mayor que 0 -> isinstance comprueba tipos de datos
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")


carlos = Persona("Carlos", 1)
print(carlos.get_nombre())
