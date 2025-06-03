'''
Clase:        Clase 10
Tema:         Arrays

Autor:        Juan Pablo Quintanilla
Fecha:        2025-06-03
Estado:       [ Terminado ]
'''
import numpy as np

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

zeros = np.zeros(5)
print(zeros)

ones = np.ones(5)
print(ones)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2

resultado = arr1 * arr2

arr = np.array([1, 2, 3])
result = arr + 5

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
# Recupera los elementos donde la condición es verdadera: [3, 4, 5]

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 
# Recupera los elementos en los índices especificados: [1, 3, 5]

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
]) 

print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo .dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miercoles (dia 3):", consumo[:, 2])

promedio_por_hogar = np.mean(consumo, axis = 1)

promedio_por_dia  = np.mean(consumo)

total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

maximos = np.max(consumo, axis = 1)

minimos = np.min(consumo, axis = 0)

desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

consumo_total_hogar = np.sum(consumo, axis = 1)

hogar_mayor_consumo = np.argmax(consumo_total_hogar)

hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

consumo_total_hogar = np.sum(consumo, axis = 1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

altos = consumo_total_hogar > 100

consumo_mayor_100 = np.where(altos)[0]
print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

consumo_noramlizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())
print(consumo_noramlizado)

'''
1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)? 
2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total
'''

# 1. Consumo del hogar 5 el viernes (día 5, índice 4)
consumo_hogar5_viernes = consumo[4, 4]
print(f"1. Consumo del hogar 5 el viernes: {consumo_hogar5_viernes}")

# 2. Consumo de los últimos 3 hogares el domingo (columna 6)
ultimos3_domingo = consumo[-3:, 6]
print(f"2. Consumo de los últimos 3 hogares el domingo: {ultimos3_domingo}")

# 3. Promedio de consumo los fines de semana (sábado y domingo → columnas 5 y 6)
fines_de_semana = consumo[:, [5, 6]]
promedio_fines_semana = np.mean(fines_de_semana)
print(f"3. Promedio de consumo en fines de semana: {promedio_fines_semana:.2f}")

# 4. Día con mayor desviación estándar
desviaciones_dia = np.std(consumo, axis=0)
dia_mayor_desv = np.argmax(desviaciones_dia)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
print(f"4. Día con mayor desviación estándar: {dias[dia_mayor_desv]} ({desviaciones_dia[dia_mayor_desv]:.2f})")

# 5. Los 3 hogares con menor consumo total
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print(f"5. Índices de hogares con menor consumo: {indices_menor_consumo}")
print(f"   Valores de consumo: {valores_menor_consumo}")

# 6. Nuevo consumo total del hogar 3 con aumento del 10% diario
hogar3 = consumo[2]
hogar3_aumentado = hogar3 * 1.10
nuevo_total_hogar3 = np.sum(hogar3_aumentado)
print(f"6. Nuevo consumo total del hogar 3 con aumento del 10%: {nuevo_total_hogar3:.2f}")