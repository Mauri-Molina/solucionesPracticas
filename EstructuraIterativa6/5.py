# Ejercicio 5: Generar la tabla de multiplicar usando while

num = int(input("Ingrese un número entre 1 y 10: "))

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1