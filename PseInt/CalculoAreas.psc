Algoritmo CalculoAreas
	
    // Declarar variables
    Definir baseRectangulo Como Real
    Definir alturaRectangulo Como Real
    Definir areaRectangulo Como Real
    Definir baseTriangulo Como Real
    Definir alturaTriangulo Como Real
    Definir areaTriangulo Como Real
	
    // Calcular área del rectángulo
    Escribir "Ingrese la base del rectángulo: "
    Leer baseRectangulo
    Escribir "Ingrese la altura del rectángulo: "
    Leer alturaRectangulo
    areaRectangulo <- baseRectangulo * alturaRectangulo
    Escribir "El área del rectángulo es: ", areaRectangulo
	
    // Calcular área del triángulo
    Escribir "Ingrese la base del triángulo: "
    Leer baseTriangulo
    Escribir "Ingrese la altura del triángulo: "
    Leer alturaTriangulo
    areaTriangulo <- (baseTriangulo * alturaTriangulo) / 2
    Escribir "El área del triángulo es: ", areaTriangulo
	
FinAlgoritmo
