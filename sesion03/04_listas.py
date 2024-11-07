# Colección ordenada, modificable y mutable

lista = []   # lista vacía
lista_nombres = ["Carlos", "Arturo", "Julia"]
lista_nombres[0] = "C4rlos"
print(lista_nombres)

# Ejemplo de iteración en una lista con bulce for

for nombre in lista_nombres:
    print(nombre)

# append() añade un elemento al final de la lista
# insert() lo añade en una posición concreta
# remove() elimina X valores de la lista
# pop() elimina el ultimo valor de la lista
# __delitem__() elimina los datos de la lista
# del [lista] elimina la lista


for nombre in lista_nombres:
    if nombre == "Arturo":
        lista_nombres.remove(nombre)

print(lista_nombres)