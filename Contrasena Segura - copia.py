'''
Clase:        Clase 2
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Contrasena Segura
Descripción:  Definición del ejercicio

Autor:        Juan Pablo Quintanilla
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''

contra = input("Escribe tu contrasena: ")
sinumero = False
simayus = False

for caracter in contra:
    if caracter.isdigit():
        sinumero = True
    if caracter.isupper():
        simayus = True  

if sinumero and simayus and len(contra) < 8 == True:
    print ("Contrasena Segura")
else:
    print("Contrasena No Segura")