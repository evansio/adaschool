"""Parte 2: Carga de datos
Continuando con la anterior sección del proyecto integrador, ahora debes realizar lo siguiente:

1- Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.

2- Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.

3- Calcular los promedios de las edades de cada dataset e imprimir."""

from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")

# Obtener la partición de entrenamiento
data = dataset["train"]

# Ver la estructura del conjunto de datos
print(data)

import numpy as np

# Obtener la lista de edades
edades = data['age']

# Convertir la lista a un arreglo de NumPy
edades_np = np.array(edades)

import pandas as pd

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el dataframe en dos basados en la columna 'is_dead'
df_fallecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

# Calcular el promedio de edades para cada dataset
promedio_edad_fallecidos = df_fallecidos['age'].mean()
promedio_edad_sobrevivientes = df_sobrevivientes['age'].mean()

# Imprimir los resultados
print(f"Promedio de edad de personas que fallecieron: {promedio_edad_fallecidos} años")
print(f"Promedio de edad de personas que sobrevivieron: {promedio_edad_sobrevivientes} años")