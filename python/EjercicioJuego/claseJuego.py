class Juego:
    def __init__(self, vidas,puntos, nivel):
            self.vidas = vidas
            self.puntos = puntos
            self.nivel = nivel

    def ObtenerVidas(self):
        return self.vidas

    def obtenerPuntos(self):
        return self.puntos
    def obtenerNivel(self):
        return self.nivel
    def sumarPuntos(self, puntos):
        self.puntos += puntos
    def modificarVidas(self, vidas):
        self.vidas -= vidas
    def modificarPuntos(self, puntos):
        self.puntos -= puntos
    def modificarNivel(self, nivel):
        self.nivel += nivel

    def validarVidas(self):
        if self.vidas == 0:
            print("lo lamento te quedaste sin vidas,vuelve a intentarlo")
            exit()
    def compraPista(self):
        pistas = [
            # Nivel 1
            ["pista 1. Tiene visión pero no es un ser vivo",
             "pista 2. Es grande y de madera", 
             "pista 3. Marca el tiempo", 
             "pista 4. Se utiliza para subir o bajar", 
             "pista 5. Se extiende por kilómetros"],

            # Nivel 2
            ["pista 1. Se envía por correo",
             "pista 2. Es un curso de agua", 
             "pista 3. Es un número que nunca disminuye", 
             "pista 4. Se llena y se vacía", 
             "pista 5. Es un sonido muy suave"],

            # Nivel 3
            ["pista 1. Te dice la hora", 
             "pista 2. Se utiliza para desenredar", 
             "pista 3. Soporta objetos", 
             "pista 4. Genera energía", 
             "pista 5. Lo usamos para vaciar cosas"],

            # Nivel 4
            ["pista 1. Es un órgano", 
             "pista 2. Se encuentra en los bosques", 
             "pista 3. Se usa para guardar alimentos", 
             "pista 4. Sostiene cosas", 
             "pista 5. Lo abres para leer"],

            # Nivel 5
            ["pista 1. Lo encuentras en el suelo", 
             "pista 2. Siempre esperamos por él", 
             "pista 3. Es una imagen impresa",  
             "pista 4. Es un tubérculo", 
             "pista 5. Lo atrapas durante el invierno"]
        ]
        print(f"Bienvenido ala tienda de pistas\nUsted tiene {self.obtenerPuntos()} de puntos")
        opcion = int(input("1.Comprar pistas\n0.salir "))
        if(opcion == 1):
            self.modificarPuntos(200)
            nivel = self.nivel
            opcion2 = int(input("cada pista que quieras tiene un costo 200 puntos \nmarca el numero de pregunta que quieres "))
            if 0 <= opcion2 <= 5:
                print(pistas[nivel][opcion2 - 1 ])
            else:
                print("Selección no válida.")
        else:
            print("En otra ocacion")




        
    def PrimerNivel(self):
        acertijos_1 = {
            "1. ¿Qué tiene ojos pero no puede ver?": "una papa",
            "2. ¿Qué tiene llaves pero no abre puertas?": "un piano",
            "3. ¿Qué tiene agujas pero no puede coser?": "un reloj",
            "4. ¿Qué va de arriba a abajo sin moverse?": "una escalera",
            "5. ¿Qué tiene ramas pero no es un árbol?": "una carretera"
        }
        print("Bien estas en el primer nivel  ")
        for pregunta, respuesta in acertijos_1.items():
            self.validarVidas()
            print(pregunta)
            if self.obtenerPuntos() >= 300:
                self.compraPista()
            opcion = input().lower()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(100)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)
        self.modificarNivel(1)
        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    def SegundoNivel(self):
        acertijos_2 = {
            "1. ¿Qué tiene alas pero no puede volar?": "una carta",
            "2. ¿Qué es siempre viejo y nunca joven?": "un rio",
            "3. ¿Qué siempre sube y nunca baja?": "la edad",
            "4. ¿Qué es lo que puede estar lleno o vacío pero nunca medio lleno?": "un agujero",
            "5. ¿Qué se puede romper sin tocarlo?": "un susurro"
        }
        print("Bien estas en el segundo nivel  ")
        for pregunta, respuesta in acertijos_2.items():
            self.validarVidas()
            print(pregunta)
            if self.obtenerPuntos() >= 300:
                self.compraPista()
            opcion = input().lower()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(100)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)
        self.modificarNivel(1)
        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    
    def TercerNivel(self):
        acertijos_3 = {
            "1. ¿Qué tiene manos pero no puede aplaudir?": "un reloj",
            "2. ¿Qué tiene dientes pero no puede morder?": "un peine",
            "3. ¿Qué tiene una sola pata pero puede caminar?": "una mesa",
            "4. ¿Qué tiene ruedas y vuelta sin moverse?": "un molino de viento",
            "5. ¿Qué es lo que se hace más grande cuanto más se quita de él?": "un agujero"
        }
        print("Bien estas en el tercer nivel  ")
        for pregunta, respuesta in acertijos_3.items():
            self.validarVidas()
            print(pregunta)
            if self.obtenerPuntos() >= 300:
                self.compraPista()
            opcion = input().lower()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(100)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)
        self.modificarNivel(1)
        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    def CuartoNivel(self):
        acertijos_4 = {
            "1. ¿Qué es lo que puedes romper, incluso si nunca lo has tocado o visto?": "un corazón",
            "2. ¿Qué tiene muchas agujas pero no puede coser?": "un pino",
            "3. ¿Qué es lo que tiene siempre la boca abierta?": "un frasco",
            "4. ¿Qué tiene patas pero no puede caminar?": "una mesa",
            "5. ¿Qué tiene hojas pero no es un árbol?": "un libro"
        }
        print("Bien estas en el cuarto nivel  ")
        for pregunta, respuesta in acertijos_4 .items():
            self.validarVidas()
            print(pregunta)
            if self.obtenerPuntos() >= 300:
                self.compraPista()
            opcion = input().lower()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(100)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)
        self.modificarNivel(1)
        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    def  QuintoNivel(self):
        acertijos_5 = {
            "1. ¿Qué tiene un fondo pero no un lado?": "un agujero",
            "2. ¿Qué es lo que siempre está en camino pero nunca llega?": "mañana",
            "3. ¿Qué puede viajar alrededor del mundo sin moverse?": "un sello",
            "4. ¿Qué tiene ojos pero no puede ver?": "una papa",
            "5. ¿Qué es lo que se puede coger pero nunca se tira?": "un resfriado"
        }
        print("Bien estas en el quinto nivel  ")
        for pregunta, respuesta in acertijos_5.items():
            self.validarVidas()
            print(pregunta)
            if self.obtenerPuntos() >= 300:
                self.compraPista()
            opcion = input().lower()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(100)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)
        print(f"Felicidades usted a completado el juego")
        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')
        exit()



