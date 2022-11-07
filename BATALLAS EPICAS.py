
import random

def rand(a,b):
    """funcion q retorna un valor de ataque dentro del rango del personaje"""
    return random.randint(a,b)

def comienzo():
    print()
    print("Desarrollado por los alumnos:".center(100))
    print("Simón Ottati, Bernabé Zelaya, Giuliano Politi, Marcos León".center(100))
    print()
    print("BATALLAS EPICAS".center(100))
    print()
    print("1) Batalla 1vs1".center(100))
    print("2) Como jugar".rjust(55))
    print("3) Salir".rjust(50))
    print()
    while True:
        try:
            entrada = int(input("Elija una opcion aqui >>>> ")) 
            assert entrada >= 1 and entrada <= 4
            return entrada
        except ValueError:
            print("Error. Ingresar 1, 2 o 3.", end=" ")

def comoJugar():
    print("Es un juego desarrollado por los alumnos, que consiste en una batalla épica como bien lo llama el nombre.\n")
    print("Hay distintos personajes icónicos. Se basa en una batalla por turnos\n")
    print("Hay 3 opciones para elegir, estas son:")
    print("Ataque básico: opcion 1, el personaje elegido ataca en un determinado rango, el valor dentro de ese rango es al azar\n")
    print("Curación: opcion 2, el personaje se cura a si mismo cierta cantidad de vida\n")
    print("Definitiva: se puede lanzar cada 3 turnos. Hay cierta probabilidad de falla, cada personaje tiene su porcentaje.")
    print("Se puede fallar, pero al fallarla, pierdes el turno. Pero sigues teniendo la definitiva disponible para el proximo turno.")
    print("Aunque puedes fallarla nuevamente, es algo riesgoso pero fulminante.\n")

    entrada = input("Enter para volver al menu.")
    while entrada != "":
        print("Ingreso invalido.")
        entrada = input("Enter para volver al menu.")

def personajes():
    personajes  = {
        "Charizard": ["Charizard", 250, [28, 38], 35, 85, [1,200]],
        "Mario": ["Mario", 280, [25,32], 30, 70, [1,250]],
        "Tauros": ["Tauros", 225, [33,43], 25, 70, [1,250]],
        "Spiderman": ["Spiderman", 300, [20,25], 30, 50, [1,260]],
        "Harry Potter": ["HarryPotter", 180, [44,54] ,40, 100, [1,200]],
        "Goku": ["Goku", 210, [39,46], 40, 70, [1,250]],
        "Vegetta": ["Vegetta", 250, [30,36], 32, 80, [1,220]],
        "Pikachu": ["Pikachu", 230, [24, 40], 35, 78, [1, 200]],
        "Iron Man": ["IronMan", 270, [28, 34], 38, 82, [1, 250]],
        "Venom": ["Venom", 260, [26, 38], 36, 75, [1, 200]]
    }
    print("Personajes disponibles para elegir:")
    print()
    for personaje in personajes:
        print(personaje.center(10), end="")
    print()
    print()
    try:
        print("Quiere saber las estadisticas de todos los personajes?")
        decision = int(input("Ingrese 0 para verlas, cualquier caracter para continuar: "))
        print()
        assert decision == 0, "Valor inválido."
        columnas = len((personajes)["Goku"][:]) 
        filas = len((personajes).keys()) 
        matriz = [[0] * columnas for i in range(filas)]
        lista = ["PERSONAJES", "VIDA", "RANGO BÁSICO", "CURACIÓN", "DEFINITIVA", "PROBABILIDAD DEFINITIVA"]
        listapersonajes = list(personajes.keys())
        listapersonajes.insert(0, "")
        for i in range(filas):
            for j in range(columnas):
                matriz[0][j] = lista[j]
                matriz[i][0] = listapersonajes[i]
                datos = list(personajes.get(listapersonajes[i+1]))
                matriz[i][j] = datos[j]
                matriz[i][columnas-1] = str(int((datos [5][1] - 100) /2)) + "%"
        prolijidad = 0
        for i in range(filas):
            for j in range(columnas):
                print(str(matriz[i][j]).strip("[]").center(prolijidad+15), end="")
            print()
    except AssertionError:
        pass
    except ValueError:
        pass
    return personajes

def elegirPokemones(nombre, personajes):
    print()
    while True:
        try:
            ent = input(f"{nombre}, ingresar nombre del pokemon: ").title()
            assert ent in personajes, "Pokemon no encontrado."

            print(f"Elegiste a {ent}! Estas son sus estadisticas:")
            print()
            print(f"Vida: {personajes[ent][1]}".center(25), end="")
            print(f"Ataque: {personajes[ent][2][0]}, {personajes[ent][2][1]}".center(25), end = "")
            print(f"Curación: {personajes[ent][3]}".center(25), end="")
            print(f"Definitiva: {personajes[ent][4]}".center(25))
            print()

            seleccion = int(input("Ingresar 0 para confirmar eleccion o 1 para volver a elegir otro personaje: "))
            
            
            while seleccion <= 0 and seleccion >= 1:
                print("Numero invalido. Elegir una opcion correcta.")
                seleccion = int(input("Ingresar 0 para confirmar eleccion o 1 para volver a elegir otro personaje: "))

            else:
                if seleccion == 0:
                    return personajes[ent]
                    
                
            assert seleccion != 1, "Eleccion cancelada."

            False
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Ingresar solo 1 u 2.")

def habilidades():
    while True:
        try:
            print("Ingrese 2 para ataque comun, 3 para curacion, y 4 para la definitiva")
            decision = int(input("Que accion desea realizar?: "))

            assert 2 <= decision <= 4

            if decision == 2:
                return 2
            elif decision == 3:
                return 3
            elif decision == 4:
                return 4

        except AssertionError:
            print("Ingresar una opcion valida.")
        except ValueError:
            print("Ingresar una opcion valida.")
        
def jugadorVsJugador():
    nombreJugador1 = input("Ingresar nombre del jugador 1: ")
    while not nombreJugador1.isalnum():
        print("Nombre invalido. Ingrese un nombre de usuario alfanumerico sin espacios")
        nombreJugador1 = input("Ingresar nombre del jugador 1: ")
    pokemonJugador1 = elegirPokemones(nombreJugador1, personajes())
    nombreJugador2 = input("Ingresar nombre del jugador 2: ")
    while not nombreJugador2.isalnum():
        print("Nombre invalido. Ingrese un nombre de usuario alfanumerico sin espacios")
        nombreJugador2 = input("Ingresar nombre del jugador 2: ")
    pokemonJugador2 = elegirPokemones(nombreJugador2, personajes())

    return nombreJugador1, pokemonJugador1, nombreJugador2, pokemonJugador2

def partida(jugador1, personaje1, jugador2, personaje2):
    
    turno = 0
    print()

    print(jugador1.ljust(40), "JUGADORES".center(18), jugador2.rjust(40))

    print(str(personaje1[0]).ljust(40), "PERSONAJE".center(18), str(personaje2[0]).rjust(40))

    print()

    print(str(personaje1[1]).ljust(40), "VIDA".center(18), str(personaje2[1]).rjust(40))

    print(str(personaje1[2]).strip("[]").ljust(40), "RANGO ATAQUE".center(18), str(personaje2[2]).strip("[]").rjust(40))

    print(str(personaje1[3]).ljust(40), "CURACION".center(18), str(personaje2[3]).rjust(40))

    print(str(personaje1[4]).ljust(40), "ULTI".center(18), str(personaje2[4]).rjust(40))

    vidaPersonaje1 = personaje1[1]
    vidaPersonaje2 = personaje2[1]

    # [tipo, vida, ataque, curacion, ulti]
    contador1 = 0
    contador2 = 0
    while vidaPersonaje1 > 0 and vidaPersonaje2 > 0:
        print()
        if turno == 0:
            print(f"Turno de {jugador1}:")
            accion = habilidades()
            contador1 += 1
            while accion == 4 and contador1 < 3:
                print("La definitiva la tiene cada 3 turnos y aun no esta disponible, ingrese otra habilidad.")
                accion = habilidades()
            if accion == 3:
                vidaPersonaje1 += personaje1[accion]
            elif accion == 4:
                if rand(personaje1[5][0], personaje1[5][1]) >= 100:
                    vidaPersonaje2 -= personaje1[accion]
                    contador1 = 0
                else:
                    contador1 = 3
                    print("Has fallado la definitiva. Pierdes el turno.")
                    
            else:
                vidaPersonaje2 -= rand(personaje1[accion][0], personaje1[accion][1])

            turno = 1
            print()
            print(f"Vida de {str(personaje1[0])} {str(vidaPersonaje1)}".ljust(50), end = "")
            print(f"Vida de {str(personaje2[0])} tras el ataque {str(vidaPersonaje2)} ".rjust(50))

        else:
            print(f"Turno de {jugador2}:")
            accion = habilidades()
            contador2 += 1
            while accion == 4 and contador2 < 3:
                print("La definitiva la tiene cada 3 turnos y aun no esta disponible, ingrese otra habilidad.")
                accion = habilidades()
            
            if accion == 3:
                vidaPersonaje2 += personaje2[accion]
            elif accion == 4:
                if rand(personaje2[5][0], personaje2[5][1]) >= 100:
                    vidaPersonaje1 -= personaje2[accion]
                    contador2 = 0
                else:
                    print("Has fallado la definitiva. Pierdes el turno")
                    contador2 = 3
            else:
                vidaPersonaje1 -= rand(personaje2[accion][0], personaje2[accion][1])

            turno = 0
            print()
            print(f"Vida de {str(personaje1[0])} tras el ataque {str(vidaPersonaje1)}".ljust(50), end = "")
            print(f"Vida de {str(personaje2[0])} {str(vidaPersonaje2)} ".rjust(50))
            
    if vidaPersonaje1 > 0:
        ganador = jugador1
        perdedor = jugador2
        print(f"{jugador1} con {personaje1[0]}, gano!".center(100))
        print(f"{jugador2} con {personaje2[0]}, perdio.".center(100))
        print()
    else:
        ganador = jugador2
        perdedor = jugador1
        print(f"{jugador2} con {personaje2[0]}, gano!".center(100))
        print(f"{jugador1} con {personaje1[0]}, perdio.".center(100))
        print()

    return ganador, perdedor

def jugadorVsPc():
    pass



                
historialJugadores = []
numPartida = 0
while True:
    try:
        modoDeJuego = comienzo()
        if modoDeJuego == 1:
            nombre1, personaje1, nombre2, personaje2 = jugadorVsJugador()
            ganador, perdedor = partida(nombre1, personaje1, nombre2, personaje2)
            numPartida += 1
            historialJugadores.append([numPartida, ganador, perdedor])
            
            
            jugar = input("Presione enter para volver a jugar, o cualquier caracter para salir: ")
            assert jugar != ""
            print("Gracias por jugar.")
            break
        elif modoDeJuego == 2:
            retorno = comoJugar()
            assert retorno != ""

        elif modoDeJuego == 3:
            print("Hasta la proxima!")
            break
    except AssertionError:
        modoDeJuego == 1
    except KeyboardInterrupt:
        print("\n Has interrumpido el juego.")
        break
try:
    historial = open("historial.txt", "wt")

    for partida in historialJugadores:
        historial.write(f"Partida {partida[0]}: {partida[1]} gano, {partida[2]} perdio. \n")

except FileNotFoundError:
    print("No se puede grabar el archivo:")
finally:
    try:
        historial.close()
    except NameError:
        pass
