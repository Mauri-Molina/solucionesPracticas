Algoritmo DeterminarMayorDeTresNumeros
	
    // Declarar variables
    Definir num1, num2, num3 Como Entero
	
    // Leer los n�meros
    Escribir "Ingrese el primer n�mero: "
    Leer num1
    Escribir "Ingrese el segundo n�mero: "
    Leer num2
    Escribir "Ingrese el tercer n�mero: "
    Leer num3
	
    // Determinar el mayor n�mero
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
