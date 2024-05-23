# Ejercicio 5: Calcular el costo de la leche con descuentos

# Solicitar datos de entrada
unidades_de_leche = int(input("Ingrese la cantidad de unidades de leche: "))
es_jubilado = input("¿Es jubilado? (si/no): ").strip().lower() == 'si'

# Calcular el monto parcial
monto_parcial = unidades_de_leche * 1000

# Calcular el monto a pagar según los descuentos
if unidades_de_leche > 24:
    monto_a_pagar = monto_parcial * 0.85
elif unidades_de_leche > 12:
    monto_a_pagar = monto_parcial * 0.9
else:
    monto_a_pagar = monto_parcial

# Aplicar descuento adicional si es jubilado
if es_jubilado:
    monto_a_pagar *= 0.9

# Mostrar el resultado
print("El monto a pagar es:", monto_a_pagar)
