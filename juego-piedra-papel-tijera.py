nombre1 = input("Ingrese el nombre del jugador 1: ")
nombre2 = input("Ingrese el nombre del jugador 2: ")

jugador1 = input("Jugador 1, elige piedra, papel o tijera: ")
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ")

condicion1 = (jugador1 == "piedra" and jugador2 == "tijera")
condicion2 = (jugador1 == "papel" and jugador2 == "piedra")
condicion3 = (jugador1 == "tijera" and jugador2 == "papel")

if jugador1 == jugador2:
    print("¡Es un empate!")
elif condicion1 or condicion2 and condicion3:
    print("ha ganado:", nombre1)
else:
    print("ha ganado:", nombre2)