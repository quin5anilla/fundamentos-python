'''
Clase:        Clase 1
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Calcular Impuestos
Descripción:  Definición del ejercicio

Autor:        Juan Pablo Quintanilla
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''

total_cuenta = float(input("Ingrese el total de su cuenta: "))
impuesto_aplicado = float(input("Ingrese su porcentaje de propina: "))
cuenta_impuesto = total_cuenta + total_cuenta * (impuesto_aplicado/100)
print(f"Tu cuenta total fue de: {cuenta_impuesto:.2f}") #El .2 significa el numero de decimales que quiero y f es float