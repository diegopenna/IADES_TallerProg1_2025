def estadoAlumno(nombre, apellido, *notas,  materia = "", promociona = 7):
    print(f"Alumno: {apellido}, {nombre}")
    
    if (materia != ""):
        print(f"Materia: {materia}")
    
    print("Detalle notas:")

    suma = 0
    cant = 0
    for nota in notas:
        cant = cant + 1
        suma = suma + nota
        print(f"Nota {cant}: {nota}")
    
    promedio = round(suma / cant, 2)
    print(f"Promedio final: {promedio}")

    if (promedio >= promociona):
        print("Promociona la materia")
    else:
        print("No Promociona la materia. Debe rendir final")
    
estadoAlumno("Pepito", "Perez", 5, 8, 6, materia="Programacion 1")


