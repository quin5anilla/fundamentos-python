'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    Numero Magico
Descripción:  Definición del ejercicio

Autor:        Juan Pablo Quitanilla
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''

num = int(input("Ingrese un numero: "))
if num % 7 == 0 and num % 5 != 0: 
    print("Magico")
else:
    print("No Magico")