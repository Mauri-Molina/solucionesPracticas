# Gestión de una agenda telefónica
agenda = {}

def agregar_persona():
    dni = input("Ingrese el DNI: ")
    if dni in agenda:
        print("La persona con ese DNI ya existe.")
        return
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[dni] = {"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono}
    print("Persona agregada exitosamente.")

def modificar_persona():
    dni = input("Ingrese el DNI de la persona a modificar: ")
    if dni not in agenda:
        print("La persona con ese DNI no existe.")
        return
    print("Datos actuales:", agenda[dni])
    nombre = input("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ")
    apellido = input("Ingrese el nuevo apellido (o presione Enter para mantener el actual): ")
    email = input("Ingrese el nuevo email (o presione Enter para mantener el actual): ")
    telefono = input("Ingrese el nuevo número de teléfono (o presione Enter para mantener el actual): ")
    if nombre:
        agenda[dni]["nombre"] = nombre
    if apellido:
        agenda[dni]["apellido"] = apellido
    if email:
        agenda[dni]["email"] = email
    if telefono:
        agenda[dni]["telefono"] = telefono
    print("Datos de la persona modificados exitosamente.")

def eliminar_persona():
    dni = input("Ingrese el DNI de la persona a eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada exitosamente.")
    else:
        print("La persona con ese DNI no existe.")

def mostrar_agenda():
    if not agenda:
        print("La agenda está vacía.")
    else:
        for dni, datos in agenda.items():
            print(f"DNI: {dni}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Email: {datos['email']}, Teléfono: {datos['telefono']}")

def mostrar_menu():
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_persona()
    elif opcion == "2":
        modificar_persona()
    elif opcion == "3":
        eliminar_persona()
    elif opcion == "4":
        mostrar_agenda()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
