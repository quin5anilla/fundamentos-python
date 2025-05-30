'''
Clase:        Clase 5
Tema:         Bucles For & While 
Ejercicio:    Sumador de valores posicionales
Descripción:  Pide un numero y suma sus digitos hasta que quede uno

Autor:        Juan Pablo Quintanilla
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''


numero = int(input("Ingresa un número: "))

print(f"Tu numero es: {numero}")

while numero >= 10:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    print(f"{numero} = {suma}")
    numero = suma

print(f"El resultado fue: {numero}")
