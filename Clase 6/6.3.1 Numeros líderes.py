'''
Clase:        Clase 5
Tema:         Manejo de Listas
Ejercicio:    Numeros Ideales 
Descripcion:  Crear una lista de numeros, en la que te diga que numeros son lideres
              (Para que un numero sea lider, tiene que ser mayor que el numero a su derecha)

Autor:        Juan Pablo Quintanilla
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

entrada = entrada = input("Ingrese elementos para esta lista: ").split()  
numeros = [int(num) for num in entrada]  

lideres = []

for num in range(len(numeros) - 1):
    if numeros[num] > numeros[num + 1]:
        lideres.append(numeros[num])

lideres.append(numeros[-1])

print("Estos son los numeros lideres:", lideres)