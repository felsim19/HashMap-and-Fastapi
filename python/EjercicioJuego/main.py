from claseJuego import Juego

jugador = Juego(5,0,0)
x = True
while(x):
    opcion = str(input("Bienvenido Jugador\npara iniciar la partida marca s, para continuar "))
    if (opcion.lower() != "s"):
        print("Vuelva pronto")
        x = False
    else:
        print("Las reglas para esta aventura son las siguientes:\n1.Usted Iniciara con 5 vidas\n2.A medida de que vayas resolviendo las preguntas correctamente ganara puntos\n3.usted solo va a tener 3 pistas a si que uselas sabiamente ")
        jugador.PrimerNivel()
        jugador.SegundoNivel()
        jugador.TercerNivel()
        jugador.CuartoNivel()
        jugador.QuintoNivel()
        
