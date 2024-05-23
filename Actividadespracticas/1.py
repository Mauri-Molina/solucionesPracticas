# 1. Pedir 10 nombres no repetidos y guardarlos en una lista
nombres = []
while len(nombres) < 10:
    nombre = input("Ingrese un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("El nombre ya está en la lista, ingrese un nombre diferente.")
print("Lista de nombres ingresados:", nombres)

# 2. Eliminar la tercera y la última persona, ordenar la lista y mostrarla
if len(nombres) >= 3:
    nombres.pop(2)  # Eliminar la tercera persona (índice 2)
nombres.pop()  # Eliminar la última persona
nombres.sort()  # Ordenar la lista
print("Lista de nombres después de eliminar y ordenar:", nombres)

# 3. Guardar los datos de una persona en un diccionario
persona = {
    "nombre": input("Ingrese el nombre: "),
    "apellido": input("Ingrese el apellido: "),
    "dni": input("Ingrese el DNI: "),
    "email": input("Ingrese el email: "),
    "fecha_nacimiento": input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
}
print("Datos de la persona:", persona)

# 4. Guardar 4 personas en un diccionario de familia
familia = {}
for i in range(1, 5):
    persona = {
        "nombre": input(f"Ingrese el nombre de la persona {i}: "),
        "apellido": input(f"Ingrese el apellido de la persona {i}: "),
        "dni": input(f"Ingrese el DNI de la persona {i}: "),
        "email": input(f"Ingrese el email de la persona {i}: "),
        "fecha_nacimiento": input(f"Ingrese la fecha de nacimiento de la persona {i} (DD/MM/AAAA): ")
    }
    familia[f"persona_{i}"] = persona
print("Datos de la familia:", familia)

# 5. Guardar los primeros n números pares en una tupla y mostrarlos
n = int(input("Ingrese el valor de n: "))
numeros_pares = tuple(i for i in range(n*2) if i % 2 == 0)
print("Tupla de los primeros", n, "números pares:", numeros_pares)
