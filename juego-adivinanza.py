

import random


numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinanza")

while not adivinado :
    if not cant_intentos < cant_max_intentos:
        print("Lo siento, has agotado tus intentos")
        break

    entrada = input("Adivina el número (entre 0 y 100): ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        adivinado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

    cant_intentos += 1