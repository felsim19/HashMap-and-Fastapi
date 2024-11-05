from ejercicio1_poo import Estudiante

documento = input("Digite el numero del documento ")
nombre = input("Digite su nombre ")
apellido = input("Digite su apellido ")
correo = input("Digite su correo ")
celular = input("Digite su celular ")
edad = int(input("Digite su edad "))

estudianteUno = Estudiante(documento, nombre, apellido, correo, celular, edad)

print(f"el documento de la base de datos es {estudianteUno.obtenerdocumento()}")
print(f"el nombre de la base de datos es {estudianteUno.obtenernombre()}")
print(f"el apellido de la base de datos es {estudianteUno.obtenerapellido()}")
print(f"el correo de la base de datos es {estudianteUno.obtenercorreo()}")
print(f"el celular de la base de datos es {estudianteUno.obtenercelular()}")
print(f"la edad de la base de datos es {estudianteUno.obteneredad()}")