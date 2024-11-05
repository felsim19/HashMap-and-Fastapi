class Libro:
    def __init__(self):
        self.lista = [
        ("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"),
        ("1984", "George Orwell", "Distopía"),
        ("Orgullo y prejuicio", "Jane Austen", "Novela romántica"),
        ("El amor en los tiempos del cólera", "Gabriel García Márquez", "Realismo mágico"),
        ("El señor de los anillos", "J.R.R. Tolkien", "Fantasía épica"),
        ("Crimen y castigo", "Fyodor Dostoevsky", "Novela psicológica"),
        ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía juvenil"),
        ("Moby Dick", "Herman Melville", "Novela de aventuras"),
        ("La metamorfosis", "Franz Kafka", "Ficción absurda"),
        ("La sombra del viento", "Carlos Ruiz Zafón", "Novela histórica y misterio")
        ]
    
    def prestar_libros(self,titulo):
        for i in range(len(self.lista)):
            if titulo == self.lista[i][0]:
                print(f"el libro {titulo} ha sido prestado")
                del self.lista[i]
                return
        print("ese libro no esta disponible")
    
    def devolver_libro(self,titulo,autor,genero):
        libro = (titulo,autor,genero)
        self.lista.append(libro)
    
    def libros_autor(self, autor):
        for i in range(len(self.lista)):
            if autor == self.lista[i][1]:
                print(self.lista[i])
    
    def libros_genero(self, genero):
        for i in range(len(self.lista)):
            if genero == self.lista[i][2]:
                print(self.lista[i])
        
    def mostrar_libros(self):
        print("libros disponibles : ")
        for i in self.lista:
            print(i)
                
