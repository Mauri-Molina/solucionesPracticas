Algoritmo CalculoAreas
	
    // Declarar variables
    Definir baseRectangulo Como Real
    Definir alturaRectangulo Como Real
    Definir areaRectangulo Como Real
    Definir baseTriangulo Como Real
    Definir alturaTriangulo Como Real
    Definir areaTriangulo Como Real
	
    // Calcular �rea del rect�ngulo
    Escribir "Ingrese la base del rect�ngulo: "
    Leer baseRectangulo
    Escribir "Ingrese la altura del rect�ngulo: "
    Leer alturaRectangulo
    areaRectangulo <- baseRectangulo * alturaRectangulo
    Escribir "El �rea del rect�ngulo es: ", areaRectangulo
	
    // Calcular �rea del tri�ngulo
    Escribir "Ingrese la base del tri�ngulo: "
    Leer baseTriangulo
    Escribir "Ingrese la altura del tri�ngulo: "
    Leer alturaTriangulo
    areaTriangulo <- (baseTriangulo * alturaTriangulo) / 2
    Escribir "El �rea del tri�ngulo es: ", areaTriangulo
	
FinAlgoritmo
