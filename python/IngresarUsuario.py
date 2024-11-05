from ejercicio2_poo import User

contador = 0
password = ""


nombre = input("Ingrese su nombre ")
correo = input("Ingrese su correo ")
usuario = input("Ingrese su nombre de usuario ")
contraseña = input("Ingrese su contraseña ")

userUno = User(nombre, correo, usuario, contraseña)

while(contador < 3 ):
    print(f"Bienvenido usuario {userUno.obtenerusuario()}, usted tiene {3 - contador} intentos para acceder con su contraseña")
    password = input("Digite su contraseña ")
    if (userUno.ValidarContraseña(password)):
        print("Felicidades, usted ha entrado al sistema")
        break
    else:
        contador += 1

if contador == 3:
    print("Usted ha sido bloqueado del sistema por no tener la contraseña incorrecta")