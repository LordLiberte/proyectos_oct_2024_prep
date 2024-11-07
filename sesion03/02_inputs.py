# input() permite al usuario intorucir datos al sistema, siempre será una string

nombre = input("Dime tu nombre: ")
altura = input("Dime tu altura en metros: ")

print(f"Se llama {nombre} y mide {altura} metros")

# Si a print le asignamos : a la variable podemos decidir la cantidad de espacios que ocupará
print(f"Te llamas {nombre:10} <- aquí hay caracteres vacios")

# Si a : le asignamos nf, siendo n un numero, establecemos los decimales
print(f"Super, {float(altura):.2f}")
