
import random

def comienzo():
    print()
    print("BATALLAS POKEMON".center(100))
    print()
    print("Batalla 1vs1 (1 ".rjust(50), end="")
    print(" 2) Batalla 1vsPC".ljust(20))
    while True:
        try:
            entrada = int(input(">>>> ")) #agregar excepcion para cuando no se pone un numero -> ValueError
            assert entrada == 1 or entrada == 2
            return entrada
            break
        except ValueError:
            print("Error. Ingresar 1 u 2.", end=" ")

def elegirPokemones(nombre):
    personajes  = {
        "Charizard": ["fuego", 250, 30, 35, 70],
        "Mario": ["luchador", 280, 25, 30, 60 ],
        "Tauros": ["normal", 225, 40,25,80],
        "Spiderman": ["superheroe", 300, 20, 30, 50],
        "Harrypotter": ["mago", 180,45,40,90],
        "Goku": ["luchador", 210, 40,40,70],
        "Vegetta": ["luchador", 250, 32, 32, 70]
    }

    # [tipo, vida, ataque, curacion, ulti]
  
    print("Personajes disponibles para elegir:")
    for personaje in personajes:
        print(personaje, end="; ")

    print()
    while True:
        try:
            ent = input(f"{nombre}, ingresar nombre del pokemon: ")
            assert ent.capitalize() in personajes, "Pokemon no encontrado."

            print(f"Elegiste a {ent}! Estas son sus estadisticas:")
            print(f"Vida: {personajes[ent][1]}")
            print(f"Ataque: {personajes[ent][2]}")

            seleccion = int(input("Ingresar 0 para confirmar eleccion o 1 para volver a elegir otro personaje: "))
            
            
            while seleccion <= 0 and seleccion >= 1:
                print("Numero invalido. Elegir una opcion correcta.")
                seleccion = int(input("Ingresar 0 para confirmar eleccion o 1 para volver a elegir otro personaje: "))

            else:
                if seleccion == 0:
                    return personajes[ent.capitalize()]
                
            assert seleccion != 1, "Eleccion cancelada."

            # return personajes[ent.capitalize()]
            False
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Ingresar solo 1 u 2.")

def habilidades():
    while True:
        try:
            print("Ingrese 2 para ataque comun, 3 para curacion, y 3 para la definitiva")
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
    pokemonJugador1 = elegirPokemones(nombreJugador1)
    nombreJugador2 = input("Ingresar nombre del jugador 2: ")
    pokemonJugador2 = elegirPokemones(nombreJugador2)

    return nombreJugador1, pokemonJugador1, nombreJugador2, pokemonJugador2

def partida(jugador1, pokemon1, jugador2, pokemon2):
    
    turno = 0
    print()

    print(jugador1.ljust(40), end="")
    print("JUGADORES".center(20), end="")
    print(jugador2.rjust(40))

    print()

    print(str(pokemon1[1]).ljust(40), end="")
    print("VIDA".center(20), end="")
    print(str(pokemon2[1]).rjust(40))
    
    print(str(pokemon1[2]).ljust(40), end="")
    print("ATAQUE".center(20), end="")
    print(str(pokemon2[2]).rjust(40))

    print(str(pokemon1[3]).ljust(40), end="")
    print("CURACION".center(20), end="")
    print(str(pokemon2[3]).rjust(40))

    print(str(pokemon1[4]).ljust(40), end="")
    print("ULTI".center(20), end="")
    print(str(pokemon2[4]).rjust(40))

    vidaPokemon1 = pokemon1[1]
    vidaPokemon2 = pokemon2[1]

    # [tipo, vida, ataque, curacion, ulti]

    while vidaPokemon1 > 0 and vidaPokemon2 > 0:
        print()
        if turno == 0:
            print(f"Turno de {jugador1}:")
            accion = habilidades()
            
            if accion == 3: #se suma la vida xq se cura
                vidaPokemon1 += pokemon1[accion]
            else: #ataca
                vidaPokemon2 -= pokemon1[accion]

            turno = 1

            print(str(vidaPokemon1).ljust(50), end="")
            print(str(vidaPokemon2).rjust(50))

            # vidaPokemon2 -= pokemon1[habilidades()]
            # turno = 1
            # print(vidaPokemon2)

        else:
            print(f"Turno de {jugador2}:")
            accion = habilidades()
            print(accion)
            
            if accion == 3:
                vidaPokemon2 += pokemon2[accion]
            else:
                vidaPokemon1 -= pokemon2[accion]

            turno = 0

            print(str(vidaPokemon1).ljust(50), end="")
            print(str(vidaPokemon2).rjust(50))
        
def jugadorVsPc():
    pass

modoDeJuego = comienzo()
if modoDeJuego == 1:
    nombre1, pokemon1, nombre2, pokemon2 = jugadorVsJugador()
    partida(nombre1, pokemon1, nombre2, pokemon2)
else:
    jugadorVsPc()
