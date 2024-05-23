Algoritmo SumaPrimerosNNumeros
	
    // Declarar variables
    Definir N, suma, i Como Entero
	
    // Leer el valor de N
    Escribir "Ingrese el valor de N: "
    Leer N
    suma <- 0
    
    // Calcular la suma de los primeros N números enteros positivos
    Para i <- 1 Hasta N Con Paso 1 Hacer
        suma <- suma + i
    FinPara
    
    // Mostrar el resultado
    Escribir "La suma de los primeros ", N, " números enteros positivos es: ", suma
	
FinAlgoritmo
