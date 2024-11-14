# Una función tiene variables internas. Aunque se llamen igual a otras fuera de la función
# esta variable no es afectada por llamarse igual. Esto son para valores unicos. En caso de listas
# estas si se modifican al pasar por funciones

def modificar_numero(numero_original):
    numero_original *= 2

numero_original = 5
print(f"Valor original antes de modificarlo: {numero_original}")
modificar_numero(numero_original)
print(f"Valor original despues de modificarlo: {numero_original}")

def modificar_lista(lista):
    lista.append(4)

lista = [1,2,3]
print(f"Valor original antes de modificarlo: {lista}")
modificar_lista(lista)
print(f"Valor original despues de modificarlo: {lista}")