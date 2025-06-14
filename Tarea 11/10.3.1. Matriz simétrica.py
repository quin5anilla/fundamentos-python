'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    Matriz Simetica
Descripción:  Crear una matriz de 4x4, que tenga caracteristicas similares en ambas diagonales

Autor:        Juan Pablo Quintanilla
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
#misma base del codigo del ejercicio de diagonal principal y secundaria
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

    if len(set(diagonal_principal)) == len(set(diagonal_secundaria)) and \
       len(diagonal_principal) - len(set(diagonal_principal)) == len(diagonal_secundaria) - len(set(diagonal_secundaria)):
        print("La matriz es simétrica")
    else:
        print("La matriz no es simetrica")