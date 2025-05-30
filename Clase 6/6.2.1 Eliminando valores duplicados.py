'''
Clase:        Clase 5
Tema:         Manejo de Listas
Ejercicio:    Eliminando valores duplicados 
Descripcion:  Crear una lista que se elimine los elementos duplicados

Autor:        Juan Pablo Quintanilla
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

entrada = input("Ingrese elementos para esta lista: ").split()  
numeros = [int(num) for num in entrada]  

repetidos = set()
resultado = []

for num in numeros:
    if num not in repetidos:
        repetidos.add(num)
        resultado.append(num)


print(' '.join(map(str, resultado)))
# Nota:Los numeros se tienen que poner separados
