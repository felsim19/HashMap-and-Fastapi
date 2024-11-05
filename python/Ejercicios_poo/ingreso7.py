from ejercicio7 import Libro

manejo_libros = Libro()

while(True):
    op = int(input("1.Mostar libros\n2.prestar libros\n3.devolver libros\n4.Buscar autor\n5.buscar genero\n6.salir\n"))
    if(op == 1):
        manejo_libros.mostrar_libros()
    elif(op == 2):
        titulo = str(input("Digite el titulo del libro que desea que le preste "))
        manejo_libros.prestar_libros(titulo)
    elif(op == 3):
        titulo = str(input("Digite el titulo del libro que va a devolver "))
        autor = str(input("Digite el autor del libro que va a devolver "))
        genero = str(input("Digite el genero del libro que va a devolver "))
        manejo_libros.devolver_libro(titulo, autor, genero)
    elif(op == 4):
        autor = str(input("Digite el nombre del autor que esta buscando "))
        manejo_libros.libros_autor(autor)
    elif(op == 5):
        genero = str(input("Digite el nombre del genero que esta buscando "))
        manejo_libros.libros_genero(genero)
    elif(op == 6):
        print("adiiiioos")
        break