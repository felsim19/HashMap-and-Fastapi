x = True

while(x):
    print("Bienvenido puedes elegir cualquiera de los siguientes 15 puntos")
    opcion = int(input("Punto 1\nPunto 2\nPunto3\nPunto4\nPunto 5\nPunto 6\nPunto 7\nPunto 8\nPunto 9\nPunto 10\nPunto 11\nPunto 12\nPunto 13\nPunto 14\nPunto 15\nPara salir preciona 0\n"))
    if(opcion == 1):
        print("Este punto es escribir una funcion que reciba una lista de numeros y devuelva un dicionario con la cantiad de veces que aparece cada numero en la lista")
        cantidad = int(input("Bienvenido ingrese la cantidad de numeros que va a ingresar a la lista "))
        numeros = []
        for p in range(cantidad):
            numero = int(input("Ingrese el numero "))
            numeros.append(numero)
        print(numeros)
        def ConvertirDiccionario(lista):
            diccionario = {}
            for i in lista:
                if i in diccionario:
                    diccionario[i] += 1
                else:
                    diccionario[i] = 1
            return diccionario
        print(ConvertirDiccionario(numeros))
    elif(opcion == 2):
        print("Este punto escribe una funcion que tome una lista de nombres y devuelva un dicionario donde las claves sean las letras inciales y los valores sean lista de nombres que comiencen con esa letra")
        cantidad = int(input("Bienvenido ingrese la cantidad de palabras que va a ingresar a la lista "))
        nombres = []
        for p in range(cantidad):
            nombre = str(input("Ingrese el nombre "))
            nombres.append(nombre)
        print(nombres)
        def convertir(lista):
            diccionario = {}
            for i in nombres:
                PrimeraLetra = i[0]
                sublista = []
                print(f"La letra es {PrimeraLetra}")
                subcantidad = int(input("Bienvenido ingrese la cantidad de nombre que va a ingresar a la lista con esa letra "))
                for x in range(subcantidad):
                    valor = str(input("Ingrese la palabra con ese nombre "))
                    sublista.append(valor)
                diccionario[PrimeraLetra] = sublista
            return diccionario
        print(convertir(nombres))
    elif(opcion == 3):
        print("Crea una funcion que reciba una lista de palabras y devulva un dicionario con la longitud de cada palabra")
        cantidad = int(input("Bienvenido ingrese la cantidad de palabras que va a ingresar a la lista "))
        palabras = []
        for p in range(cantidad):
            word = str(input("Ingrese la palabra "))
            palabras.append(word)
        print(palabras)
        def LongitudPalabras(lista):
            diccionario = {}
            for i in lista:
                diccionario[i] = len(i)
            return diccionario
        print(LongitudPalabras(palabras))
    elif(opcion == 4):
        print("Implementar una funcion que reciba dos listas de igual longitud una de claves otra de valores y devulva un diccionario")
        cantidad = int(input("Bienvenido ingrese la cantidad de claves y valores que va a ingresar a las listas "))
        claves = []
        valores = []
        for p in range(cantidad):
            keys = str(input("Ingrese la clave "))
            claves.append(keys)
            values = str(input("Ingrese el valor "))
            valores.append(values)
        print(claves)
        print(valores)
        def convertirListas(lista1,lista2):
            diccionario = {}
            for i in range(len(lista1)):
                diccionario[lista1[i]] = lista2[i]
            return diccionario
        print(convertirListas(claves, valores))
    elif(opcion == 5):
        print("desarrollar una funcion que tome una lista de estudiantes y sus calificaciones y que devuelva un dicicionario con el promedio de cada estudiante")
        cantidad = int(input("Bienvenido ingrese la cantidad de estudiantes que va a ingresar a la lista "))
        nombres = []
        notass = []
        for p in range(cantidad):
            nombre = str(input("Ingrese el nombre "))
            nombres.append(nombre)
            calif = int(input("Digite cuantas calificaiones tiene el estudiante "))
            promedio = 0
            for x in range(calif):
                notas = int(input("Digite sus calificaciones "))
                promedio += notas
            total = promedio / calif
            notass.append(total)        
        print(nombres)
        print(notass)
        def convertir(listanombre,listanotas):
            diccionario = {}
            for i in range(len(listanombre)):
                diccionario[listanombre[i]] = listanotas[i]
            return diccionario    
        print(convertir(nombres,notass))
    elif(opcion == 6):
        print("Escribir una funcion que tome un dicionario con nombres y edades y devuelva el nombre de la persona mas joven")
        cantidad = int(input("Bienvenido ingrese la cantidad de nombre y edades que va a ingresar al dicionario "))
        dicionario = {}
        for p in range(cantidad):
            name = str(input("Ingrese el nombre "))
            age = int(input("Ingrese la edad "))
            dicionario[name] = age   
        def menor(dicionario):
            minor = 999
            nameMinor = ''
            for nombre, menor in dicionario.items():
                if menor < minor:
                    minor = menor
                    nameMinor = nombre
            return minor,nameMinor
        print(menor(dicionario))
    elif(opcion == 7):
        print("Implementar una funcion que reciba una lista de numeros y devulva un dicionario con el numero como clave y valor true o false si el numero es primo")
        cantidad = int(input("Bienvenido ingrese la cantidad de numeros que va a ingresar a la lista "))
        numeros = []
        for p in range(cantidad):
            numero = int(input("Ingrese el numero "))
            numeros.append(numero)
        def devolver(lista):
            diccionario = {}
            for n in numeros:
                primo = True
                if n < 2:
                    primo = False
                else:
                    for j in range(2,int(n**0.5) + 1):
                        if n % j == 0:
                            primo = False
                            break
                diccionario[n] = primo
            return diccionario
        print(devolver(numeros))
    elif(opcion == 8):
        print("Escribir una funcion que reciba un dicionario de productos y precio  y devuelva una lista ordenada por el precio de menor a mayor")
        cantidad = int(input("Bienvenido ingrese la cantidad de productos y precios que va a ingresar al dicionario "))
        productos = {}
        for p in range(cantidad):
            product = str(input("Ingrese el producto "))
            price = int(input("Ingrese el precio "))
            productos[product] = price
        print(productos)
        def listaOrdenada(dicionario):
            lista = []
            while dicionario:
                menor_precio = 99999
                producto_menor = ''
                for producto, precio in dicionario.items():
                    if precio < menor_precio:
                        menor_precio = precio
                        producto_menor = producto
                lista.append((producto_menor, menor_precio))
                del dicionario[producto_menor] 
            return lista
        print(listaOrdenada(productos))
    elif(opcion == 9):
        print("Implementar una funcion que reciba una lista de palabras y devuelva un dicionario con las letras como clave y la plabras que contiene solo vocales como valores")
        cantidad = int(input("Bienvenido ingrese la cantidad de palabras que va a ingresar a la lista "))
        palabras = []
        for p in range(cantidad):
            numero = str(input("Ingrese el nombre "))
            palabras.append(numero)
        def palabras_con_vocales(lista):
            diccionario = {}
            vocales = 'aeiou'
            for palabra in lista:
                TieneVocal = False
                for letra in palabra:
                    if letra in vocales:
                        TieneVocal = True
                        break
                if TieneVocal:
                    PrimerLetra = palabra[0]
                    diccionario[PrimerLetra] = palabra
            return diccionario
        print(palabras_con_vocales(palabras))
    elif(opcion == 10):
        print("crea un funcion de fibonacci")
        numero = int(input("Ingrese hasta que numero desea saber "))
        def fibonacci(numero):
            fibonacci = [0,1]
            for i in range(numero):
                fibonacci.append(fibonacci[-1] + fibonacci[-2]) 
            return fibonacci
        print(fibonacci(numero))
    elif(opcion == 11):
        print("Crea una funcion que calcule la suma de los digitos de un numero y luego cuente cuantos digitos tiene la suma resultante")
        numero = int(input("Ingrese hasta que numero desea saber "))
        def calcular(numero):
            descomponer = str(numero)
            calcular = 0
            for digito in descomponer:
                calcular += int(digito)
            cantidad = str(calcular)
            total = len(cantidad)
            return calcular, total
        suma, cantidad = calcular(numero)
        print(f"El numero es {numero} y la suma de sus digitos es de {suma} y la cantidad de los digitos es de {cantidad}")
    elif(opcion == 12):
        print("Escriba una funcion que reciba un dicionario de estudiates y devuelva el estudiante con la calificacion mas alta")
        diccionario = {'Felipe': (48+50+45)/3,
               'mateo': (45+36+38)/3,
               'ferxxo': (45+39+38)/3,
               'david' : (45+46+32)/3,
               'juan' : (45+39+32)/3,
               }
        print(diccionario.items())
        def devolver(diccionario):
            NumeroMayor = 0
            estudianteM = ''
            for nombre, nota in diccionario.items():
                if nota > NumeroMayor:
                    NumeroMayor = nota
                    estudianteM = nombre
            return NumeroMayor, estudianteM
        mayor,estudiante = devolver(diccionario)
        print(f"El mayor promedio es de {mayor} y es del estudiante {estudiante}")
    elif(opcion == 13):
        print("Crea una funcion que reciba una lista de alumnos y devuelva un dicionario donde las claves sean los nombres de los cursos y los valores listas de estudiantes de esa materia ")
        materias = []
        estudiantes = []
        cantidad = int(input("Digite la cantidad de materias que va a dictar "))
        for i in range(cantidad):
            mat = str(input("Digite la materia "))
            materias.append(mat)
            cat = int(input("Digite la cantidad de estudiante que va a tener esta materia "))
            lista = []
            for j in range(cat):
                nom = str(input("Digite el nombre del estudiante "))
                lista.append(nom)
            estudiantes.append(lista)
        print(estudiantes)
        def agrupar(materias,estudiantes):
            diccionario = {}
            for i in range(len(materias)):
                diccionario[materias[i]] = estudiantes[i]
            return diccionario
        print(agrupar(materias,estudiantes))
    elif(opcion == 14):
        print("crea una funcion que reciba como entrada unas lista de palabras y devuelva una nueva lista con las palabras ordenadsa por longitu de mayor a menor")
        palabras = []
        cantidad = int(input("Digite la cantidad de palabras que va a añadir "))
        for i in range(cantidad):
            word = str(input("Ingrese las palabras "))
            palabras.append(word)
        print(palabras)
        def palabrasLongitud(lista):
            nuevalista = []
            for i in range(len(lista)):
                palabra_mayor = ""
                longitud_mayor = 0
                for x in lista:
                    if len(x) > longitud_mayor:
                        longitud_mayor = len(x)
                        palabra_mayor = x
                nuevalista.append(palabra_mayor)
                nuevalista.append(longitud_mayor)
                lista.remove(palabra_mayor)
            return nuevalista
        print(palabrasLongitud(palabras))
    elif(opcion == 15):
        print("Funcion divir una lista por sublistas")
        def listaPrincipal():
            listaPrincipal = []
            cantidad = int(input("Cuantas sublista va a tener la lista"))
            for i in range(cantidad):
                suublista = []
                cantidad = int(input("cuantos datos va a tener esta sublista?"))
                for x in range(cantidad):
                    palabras = str(input("Ingrese las palabras "))
                    suublista.append(palabras)
                listaPrincipal.append(suublista)
            return listaPrincipal
        print(listaPrincipal())
    elif(opcion == 0):
        x = False
 