#Implementa una clase `Estudiante` que contenga atributos como nombre, edad y calificaciones Permite calcular el promedio de calificaciones

from ejercicio3 import Estudiante

nombre = str(input("Binvenido usuario usted va a crear una cuenta \nPor favor ingrese su nombre\n"))
edad = int(input("Digite su edad "))
calificaiones = []
ctd = int(input("Digite la cantidad de calificaiones "))
for i in range(ctd):
    nota = float(input("Digite su calificaion "))
    calificaiones.append(nota)

estudiante1 = Estudiante(nombre,edad,calificaiones)

print(estudiante1.promedio())
print(estudiante1.to_string())
