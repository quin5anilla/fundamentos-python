'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    Juego del entorno
Descripción:  Crear una matriz, donde verifica para cada celda de una matriz binaria cuántos elementos con valor de 1 hay en las celdas vecinas  

Autor:        Juan Pablo Quintanilla
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

N = int(input("Ingrese el número de filas (N): "))
M = int(input("Ingrese el número de columnas (M): "))

matriz = []
for _ in range(N):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)
    print(matriz)

def contar_vecinos(matriz, i, j):
    count = 0
    rows = len(matriz)
    cols = len(matriz[0]) if rows > 0 else 0
    
    direcciones = [(-1,-1), (-1,0), (-1,1),
                   (0,-1),          (0,1),
                   (1,-1),  (1,0),  (1,1)]
    
    for di, dj in direcciones:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            count += matriz[ni][nj]
    
    return count

resultado = []
for i in range(N):
    fila_resultado = []
    for j in range(M):
        vecinos = contar_vecinos(matriz, i, j)
        fila_resultado.append(vecinos)
    resultado.append(fila_resultado)

for fila in resultado:
    print(f"[{','.join(map(str, fila))}]")
