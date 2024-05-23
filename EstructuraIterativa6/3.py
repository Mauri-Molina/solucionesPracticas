# Ejercicio 3: Pedir nombres de personas y mostrarlos hasta que se ingrese "fin"

while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    print(nombre)