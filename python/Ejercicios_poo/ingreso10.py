from Manejo10 import ManejoContacto

manejo_contactos = ManejoContacto()

inprogram = True

while(inprogram):
    r = int(input("Bienvenido\n1.crear Contactos\n2.Mostrar Lista\n3.Consultar Por nombre\n4.Eliminar Productos\n5.Salir\n"))
    if(r == 1):
        nombre = str(input("Ingrese el nombre "))
        telefono = str(input("Ingrese el telefono "))
        correo = str(input("Ingrese el correo "))
        manejo_contactos.AgregarContacto(nombre,telefono,correo)
    elif(r == 2):
        manejo_contactos.MostarLista()
    elif(r == 3):
        Consultar = str(input("Digite el Nombre que quiere consultar"))