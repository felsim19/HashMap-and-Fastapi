class Juego:
    vidas = 5
    puntos = 0
    nivel = 0

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
    def modificarNivel(self, nivel):
        self.nivel += nivel

    def validarVidas(self):
        if self.vidas == 0:
            print("lo lamento te quedaste sin vidas,vuelve a intentarlo")
            exit()
    def compraPista(self):
        pistas = [
            [
                "El tren eléctrico funciona con energía eléctrica, por lo que no emite humo.",
                "El cubo de hielo ya ha desplazado una cierta cantidad de agua antes de derretirse.",
                "Si enciendes ambos extremos simultáneamente, la cuerda se quemará desde ambos extremos a la vez.",
                "Puedes dividir las monedas en grupos iguales y comparar el peso de dos de los grupos.",
                "El valor esperado se calcula multiplicando cada posible resultado por su probabilidad y sumando los resultados."
            ],
            [
                "La probabilidad de sacar un as de una baraja es 1/13. Piensa en cómo se combinan estas probabilidades.",
                "Piensa en la trayectoria más corta que la hormiga puede tomar dentro del cubo.",
                "¿Qué significa 'hora correcta' en este contexto?",
                "Piensa en los múltiplos comunes de los intervalos de tiempo.",
                "Además de los triángulos formados por tres palillos, ¿puedes identificar otros patrones de triángulos?"
            ],
            [
                "Piensa en cómo se distribuirá la pintura en las caras del cubo.",
                "Encendiendo uno, apagándolo, encendiendo otro y entrando a la habitación",
                "ambos estarán igual de cocidos",
                "congelando el agua",
                "204"
            ],
            [
                "Piensa en el número mínimo de movimientos necesarios para cada cara del cubo.",
                "¿Qué sucede si sacas una fruta de la caja etiquetada incorrectamente como 'manzanas y naranjas'?",
                "¿Cómo se comporta la luz al pasar por una lupa?",
                "¿Qué sucede con el nivel del agua cuando el hielo se derrite?",
                "¿Qué posición ocupas después de adelantar al segundo corredor?"
            ],
            [
                "¿Qué sucede con la temperatura cuando una vela se apaga en una habitación cerrada?",
                "Piensa en el principio de conservación del volumen.",
                "¿Cómo cambia la posición de las manecillas en un reloj analógico si intercambias los minutos y las horas?",
                "¿Cómo puedes determinar qué interruptor controla cada bombilla sin entrar en el ático?",
                "¿Cómo se pueden unir los conceptos de distancia y número de caras en un cubo?"
            ]
        ]
        print(f"Bienvenido ala tienda de pistas\nUsted tiene {self.obtenerPuntos()} de puntos")
        opcion = int(input("1.Comprar pistas\n0.salir"))
        if(opcion == 1):
            nivel = self.nivel
            opcion2 = int(input("cada pista que quieras tiene un costo 200 puntos \n marca el numero de pregunta que quieres"))
            if 0 <= opcion2 <= 4:
                print(pistas[nivel][opcion2 - 1 ])
            else:
                print("Selección no válida.")
        else:
            print("En otra ocacion")




        
    def PrimerNivel(self):
        preguntas_respuestas_1 = {
            "1.si un tren eléctrico viaja hacia el este y el viento sopla hacia el oeste, ¿en qué dirección se desplaza el humo?": "el tren eléctrico no produce humo",
            "2.si tienes un cubo de hielo macizo y flota en un vaso de agua, después de que se derrite, ¿aumenta o disminuye el nivel del agua?": "no cambia",
            "3.tienes una cuerda de 12 metros de largo. si puedes encender un extremo de la cuerda y tarda una hora en quemarse completamente, ¿cuánto tiempo tardará en quemarse la cuerda si enciendes ambos extremos simultáneamente?": "30 minutos",
            "4.si tienes tres montones de monedas, cada uno compuesto por 30 monedas, y solo una de ellas es falsa y tiene un peso diferente, ¿cómo puedes identificar la moneda falsa utilizando una balanza de platos y solo dos pesadas?": "dividiendo las monedas en 3 grupos de 10 y comparando dos de ellos",
            "5.si tienes una caja con un 50% de probabilidad de contener un billete de 10 dólares y un 50% de probabilidad de contener uno de 5 dólares, ¿cuál es el valor esperado de abrir la caja?": "7.50 dólares"
        }
        print("Bien estas en el primer nivel  ")
        for pregunta, respuesta in preguntas_respuestas_1.items():
            self.validarVidas()
            print(pregunta)
            opcion = input()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(100)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)
            if self.obtenerPuntos() >= 200:
                self.compraPista()
        self.modificarNivel(1)
        

        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    def SegundoNivel(self):
        preguntas_respuestas_2 = {
            "si tienes una baraja de cartas y sacas tres cartas al azar, ¿cuál es la probabilidad de que las tres sean ases?": "1/221",
            "si una hormiga está en una esquina de un cubo y quiere llegar a la esquina opuesta, ¿cuál es la distancia más corta que puede recorrer?": "la longitud de una diagonal del cubo",
            "tienes un reloj analógico que muestra la hora incorrecta. a las 3:00 pm decides arreglarlo y establecer la hora correcta. si regresas después de 4 horas, ¿qué hora mostrará el reloj?": "3",
            "si colocas dos relojes uno al lado del otro, uno que avanza 1 minuto cada 2 minutos y otro que avanza 1 minuto cada 3 minutos, ¿cuánto tiempo pasará antes de que ambos relojes marquen la misma hora?": "6",
            "¿cuántos triángulos puedes formar con seis palillos de igual longitud si puedes colocarlos libremente en una superficie plana?": "8"
        }

        print("Bien estas en el segundo nivel  ")
        for pregunta, respuesta in preguntas_respuestas_2.items():
            self.validarVidas()
            print(pregunta)
            opcion = input()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(1)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)

        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')
    
    def TercerNivel(self):
        preguntas_respuestas_3 = {
            "si tienes un cubo de 6 caras y lo sumerges completamente en pintura, ¿cuántas caras tendrán al menos una porción de pintura?": "5 caras",
            "tienes tres interruptores en una habitación, cada uno de los cuales controla una bombilla en una habitación diferente. estás fuera de la habitación y solo puedes ingresar una vez. ¿cómo puedes determinar cuál interruptor controla cada bombilla?": "encendiendo uno, apagándolo, encendiendo otro y entrando a la habitación",
            "si colocas dos huevos en una sartén y los cocinas a la vez durante tres minutos, ¿cuál huevo estará más cocido, el primero o el segundo?": "ambos estarán igual de cocidos",
            "si tienes un vaso lleno de agua hasta la mitad, ¿cómo puedes agregarle más agua para que esté completamente llena sin derramar ninguna gota?": "congelando el agua",
            "si tienes un cuadrado de 5x5 formado por 25 cuadrados más pequeños, ¿cuántos cuadrados diferentes puedes formar conectando los vértices de los cuadrados pequeños?": "204"
        }

        print("Bien estas en el tercer nivel  ")
        for pregunta, respuesta in preguntas_respuestas_3.items():
            self.validarVidas()
            print(pregunta)
            opcion = input()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(1)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)

        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    def CuartoNivel(self):
        preguntas_respuestas_4 = {
            "si tienes un cubo de rubik y lo desarmas completamente, ¿cuántos movimientos diferentes necesitas para volver a ensamblarlo?": "20",
            "tienes tres cajas, una con manzanas, otra con naranjas y la última con ambas frutas. cada caja está etiquetada incorrectamente como 'manzanas', 'naranjas' o 'manzanas y naranjas'. si solo puedes sacar una fruta de una caja, ¿cómo puedes etiquetar correctamente cada caja?": "sacando una fruta de la caja etiquetada como 'manzanas y naranjas'",
            "si colocas una lupa justo en el ecuador de una esfera de cristal, ¿en qué parte de la esfera se concentra la luz?": "en el ecuador",
            "si tienes un cubo de hielo flotando en un vaso de agua y el hielo se derrite, ¿qué sucede con el nivel del agua?": "permanece igual",
            "si estás corriendo una maratón y adelantas al segundo corredor, ¿en qué posición estás ahora?": "segundo lugar"
        }

        print("Bien estas en el cuarto nivel  ")
        for pregunta, respuesta in preguntas_respuestas_4 .items():
            self.validarVidas()
            print(pregunta)
            opcion = input()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(1)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)

        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')

    def  QuintoNivel(self):
        preguntas_respuestas_5 = {
            "si tienes una vela encendida en una habitación cerrada, ¿la temperatura aumentará, disminuirá o permanecerá igual después de que se apague la vela?": "aumentará",
            "tienes un vaso lleno de agua hasta el borde. si agregas un cubo de hielo y esperas a que se derrita, ¿el agua desbordará del vaso?": "no",
            "si tienes un reloj analógico y los minutos y las horas están intercambiados, ¿a qué hora muestra el reloj cuando son las 9:15 am?": "10:45 am",
            "si tienes una caja con dos interruptores, uno enciende una bombilla en el sótano y el otro enciende una bombilla en el ático, pero no sabes qué interruptor controla cada bombilla. si solo puedes subir una vez al ático, ¿cómo puedes determinar qué interruptor controla cada bombilla?": "encendiendo uno de los interruptores durante un tiempo y luego apagándolo, y luego encendiendo el otro interruptor y subiendo al ático"
        }

        print("Bien estas en el quinto nivel  ")
        for pregunta, respuesta in preguntas_respuestas_5.items():
            self.validarVidas()
            print(pregunta)
            opcion = input()
            if opcion == respuesta:
                print("Respuesta correcta")
                self.sumarPuntos(1)
            else:
                print("Perdiste una vida")
                self.modificarVidas(1)

        print(f'Usted hizo {self.obtenerPuntos()} puntos\nY tiene {self.ObtenerVidas()} vidas')


