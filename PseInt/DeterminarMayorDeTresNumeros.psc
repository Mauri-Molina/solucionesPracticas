Algoritmo DeterminarMayorDeTresNumeros
	
    // Declarar variables
    Definir num1, num2, num3 Como Entero
	
    // Leer los números
    Escribir "Ingrese el primer número: "
    Leer num1
    Escribir "Ingrese el segundo número: "
    Leer num2
    Escribir "Ingrese el tercer número: "
    Leer num3
	
    // Determinar el mayor número
    Si num1 > num2 Entonces
        Si num1 > num3 Entonces
            Escribir "El mayor es: ", num1
        Sino
            Escribir "El mayor es: ", num3
        FinSi
    Sino
        Si num2 > num3 Entonces
            Escribir "El mayor es: ", num2
        Sino
            Escribir "El mayor es: ", num3
        FinSi
    FinSi
	
FinAlgoritmo
