'''
Clase:        Clase 5
Tema:         Bucles For & While 
Ejercicio:    Adivina el numero
Descripción:  Genera un numero aleatorio entre el 1 al 100 y pide al usuario que lo adivine

Autor:        Juan Pablo Quintanilla
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

import random

numsecret = random.randint(1, 100)
encontrado = False

print("Try if you can guess the number between 1 and 100")

while not encontrado:
    attempt = int(input("Write your number: "))

    if attempt > numsecret:
        print("The Secret Number is smaller")  # Corregí el mensaje

    elif attempt < numsecret:
        print("The Secret Number is higher")

    else:
        print(f"Congratulations, you found the secret number: {numsecret}")
        encontrado = True  
              