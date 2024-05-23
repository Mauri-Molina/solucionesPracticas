# Ejercicio 2: Mostrar solo los números pares desde 0 hasta el número ingresado

num = int(input("Ingrese un número: "))

for i in range(num + 1):
    if i % 2 == 0:
        print(i)