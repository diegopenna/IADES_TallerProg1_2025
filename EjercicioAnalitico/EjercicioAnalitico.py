"""
Realizar un programa para cargar las notas de las materias cursadas de una carrera.
Se desea registrar, el nombre de la materia, la nota de la cursada y nota de final.
Usar objetos para definir la cursada.

a)Realizar la carga. (solo el alta).
b)Calular el promedio de las notas finales y de cursada.
c)Si se promocinan las materias con 7 o mas, indicar la cantidad de materias promocionadas.
d)Mostrar la lista de cursadas ordenada por Nombre.
e)Obtener la materias con menor y mayor nota de final.
"""

class Cursada:
    def __init__(self, materia, notaCursada = 0.0, notaFinal = 0.0):
        self.materia = materia
        self.notaCursada = notaCursada
        self.notaFinal = notaFinal
    
    def __str__(self):
        return f"{self.materia :30} N.Cursada: {self.notaCursada : 6.2f} N.Final: {self.notaFinal: 6.2f}"   



listaCursadas = [
    Cursada("Matemática I", 8.5, 7.0),
    Cursada("Programación I", 9.0, 8.0),
    Cursada("Física I", 7.0, 6.0),
    Cursada("Química General", 8.0, 7.5),
    Cursada("Álgebra", 6.5, 5.0),
    Cursada("Inglés Técnico", 9.5, 9.0),
    Cursada("Análisis Matemático I", 7.8, 6.5),
    Cursada("Programación II", 8.7, 8.2),
    Cursada("Sistemas Digitales", 6.9, 7.0),
    Cursada("Estadística", 8.3, 8.0),
    Cursada("Matemática II", 7.0, 6.5),
    Cursada("Base de Datos", 9.2, 9.0),
    Cursada("Arquitectura de Computadoras", 8.1, 7.8),
    Cursada("Sistemas Operativos", 7.5, 6.0),
    Cursada("Análisis de Algoritmos", 8.6, 8.0),
    Cursada("Economía", 7.0, 7.5),
    Cursada("Redes de Computadoras", 9.1, 8.5),
    Cursada("Investigación Operativa", 6.8, 6.0),
    Cursada("Matemática Discreta", 8.4, 8.0),
    Cursada("Programación III", 9.3, 9.0),
    Cursada("Ingeniería de Software", 8.8, 8.5),
    Cursada("Bases de Datos II", 9.0, 8.7),
    Cursada("Administración de Proyectos", 7.9, 8.0),
    Cursada("Ética Profesional", 9.5, 9.8),
    Cursada("Inteligencia Artificial", 8.7, 8.5),
    Cursada("Robótica", 7.6, 7.2),
    Cursada("Seguridad Informática", 9.1, 8.9),
    Cursada("Compiladores", 8.3, 7.5),
    Cursada("Modelos y Simulación", 7.4, 7.0),
    Cursada("Proyecto Final", 9.8, 10.0),
]


#a)Realizar la carga. (solo el alta).

opc = input("Desea cargar una cursada (s,n):")

while opc == "s":
    while True:
        materia = input("Ingrese la Materia:")
        if materia != "":
            break
        else:
            print("Nombre de Materia incorrecto")
    while True:
        notaCursada = float(input("Nota Cursada:"))
        if 0 <= notaCursada <= 10:
            break
        else:
            print("Nota Cursada Incorrecta")
    while True:
        notaFinal = float(input("Nota Final:"))
        if 0 <= notaFinal <= 10:
            break
        else:
            print("Nota Final Incorrecta")
    
    unaCursada = Cursada(materia, notaCursada, notaFinal)

    listaCursadas.append(unaCursada)
    opc = input("Desea cargar otra cursada (s,n):")




#b)Calular el promedio de las notas finales y de cursada.

sumaCursadas = 0.0
sumaFinales = 0.0

for cursada in listaCursadas:
    sumaCursadas = sumaCursadas + cursada.notaCursada
    sumaFinales = sumaFinales + cursada.notaFinal

promedioCursadas = sumaCursadas / len(listaCursadas)
promedioFinales = sumaFinales / len(listaCursadas)

print(f"Promedio Cursada: {promedioCursadas : 5.2f}")
print(f"Promedio Final:   {promedioFinales : 5.2f}")

#c)Si se promocinan las materias con 7 o mas, indicar la cantidad de materias promocionadas.

promocionadas = 0

for cursada in listaCursadas:
    if cursada.notaCursada >= 7:
        promocionadas = promocionadas + 1

print(f"La cantidad de materias promocionadas es {promocionadas} de {len(listaCursadas)}.")

#d)Mostrar la lista de cursadas ordenada por Nombre.

intercambio = True
while intercambio:
    intercambio = False
    for i in range(len(listaCursadas) -1):
        if listaCursadas[i].materia > listaCursadas[i + 1].materia:
            listaCursadas[i], listaCursadas[i + 1] = listaCursadas[i + 1] , listaCursadas[i]
            intercambio = True

for cursada in listaCursadas:
    print(cursada)


#e)Obtener la materias con menor y mayor nota de final.

cursadaMenor = None
cursadaMayor = None
for cursada in listaCursadas:
    if cursadaMenor == None:
        cursadaMenor = cursada
    elif cursada.notaFinal < cursadaMenor.notaFinal:
        cursadaMenor = cursada

    if cursadaMayor == None:
        cursadaMayor = cursada
    elif cursada.notaFinal > cursadaMayor.notaFinal:
        cursadaMayor = cursada

print(f"La materia con Nota Final Menor es {cursadaMenor.materia} con un nota de {cursadaMenor.notaFinal : 6.5f}")
print(f"La materia con Nota Final Mayor es {cursadaMayor.materia} con un nota de {cursadaMayor.notaFinal : 6.5f}")



    