# Ejercicio 4: Calcular el promedio de notas y determinar el rendimiento

num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
suma_notas = 0

for i in range(num_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    suma_notas += nota 
    promedio = suma_notas / num_estudiantes

print(f"El promedio de notas es: {promedio:.2f}")

if promedio > 8:
    print("Rendimiento elevado")
elif promedio >= 6:
    print("Rendimiento aceptable")
else:
    print("Rendimiento bajo")