# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:35:08 2020

@author: 31999873
"""
import numpy as np

#%%
"""Ejercicio 4
Crear una matriz  de tamaño 6x6 en donde:
La diagonal tenga 1 (matriz A)
La antidiagonal tenga 1 (matriz B)
"""
m1 = np.arange(36).reshape((6,6))
diagonal = m1.diagonal(0)
print(diagonal)
print("***************************")
for i in range(6):
    m1[i][i] = 1

retro = 6
for j in range(6): 
    retro = retro-1
    m1[j][retro] = 1
    
print(m1)

#%%
"""
Ejercicio 5
Crear dos matrices con valores aleatorios e indicar después si tienen valores iguales
"""
m1 = np.random.randint(10, size=3)
m2 = np.random.randint(10, size=3)
datoEnComun= np.intersect1d(m1,m2)
print(m1)
print(m2)
print("Datos en comun: ")
print(datoEnComun)

#%%
"""
Ejercicio 6
Crear una matriz con valores aleatorios y hacer una función que sume los valores de cada fila
"""

m1 = np.random.randint(1,5,(5,5))
print("****MATRIZ****")
print(m1)
print("***DIAGONAL***")
print(m1.diagonal(0))

print("***********Resolucion del problema**********")

def sumarFilas(matriz):
    print(matriz)
    print(np.sum(matriz))

sumarFilas(m1)
"""
Ejercicio 7
Usando la matriz anterior sumar los valores que están en la diagonal.
"""
def sumarDiagonal(matriz):
    print(np.sum(matriz.diagonal()))

sumarDiagonal(m1)

#%%
"""
Ejercicio 8
Con la matriz creada en el ejercicio 6, modificar los primeros valores que están en cada fila, y reemplazarlos con 10.
"""
m1 = np.random.randint(1,5,(5,5))
print(m1)
print(len(m1))
print("***RESOLUCION DEL EJERCICIO***")
i_inicial = 0
i = 0
while i < len(m1):
    m1[i_inicial][i] = 10
    i += 1
    
print(m1)

#%%
"""
Ejercicio 9
Con la matriz creada en el ejercicio 6, calcular los elementos máximos y mínimos de la matriz por cada columna
"""
m1 = np.random.randint(5,10,(5,5))
print(m1)
print("******************")
valorMinimo = m1.min(axis=0)
print("El valor minimo es: ", valorMinimo)
valorMaximo = m1.max(axis=0)
print("El valor maximo es: ", valorMaximo)






