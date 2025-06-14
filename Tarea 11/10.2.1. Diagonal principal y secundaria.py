'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    Diagonal principal y secundaria
Descripción:  Crear una matriz de 4x4, y identificar las filas diagonales que posee

Autor:        Juan Pablo Quintanilla
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
#Para que la matriz sea de 4x4
N = 4

entrada = input(f"Ingrese los {N*N} números de la matriz separados por espacios: ")

numeros = list(map(int, entrada.split()))

if len(numeros) != N * N:
    print(f"Error: Debe ingresar exactamente {N*N} números.")
else:
    matriz = []
    for i in range(N):
        fila = numeros[i * N : (i + 1) * N]
        matriz.append(fila)
    
    for fila in matriz:
        print(', '.join(map(str, fila)))
    
    diagonal_principal = [matriz[i][i] for i in range(N)]
    diagonal_secundaria = [matriz[i][N - 1 - i] for i in range(N)]
    
    print("Diagonal principal:", diagonal_principal)
    print("Diagonal secundaria:", diagonal_secundaria)