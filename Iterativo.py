# Calcular la suma de los primeros N números enteros positivos

N = int(input("Ingrese el valor de N: "))
suma = 0

for i in range(1, N + 1):
    suma += i

print("La suma de los primeros", N, "números enteros positivos es:", suma)
