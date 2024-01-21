"""Parte 3: Calculando analíticas simples
Continuando con el DataFrame con todos los datos de la anterior subsección, ahora debes:

Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas)"""

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

# Verificar los tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Convertir 'is_male' y 'is_smoker' a tipo de datos booleano si es necesario
df['is_male'] = df['is_male'].astype(bool)
df['is_smoker'] = df['is_smoker'].astype(bool)

# Verificar los tipos de datos después de la conversión
tipos_de_datos_despues = df.dtypes
print("\nTipos de datos después de la conversión:")
print(tipos_de_datos_despues)

# Calcular la cantidad de hombres fumadores y mujeres fumadoras
conteo_fumadores_por_genero = df.groupby(['is_male', 'is_smoker']).size().unstack()
cantidad_hombres_fumadores = conteo_fumadores_por_genero.loc[True, True] if True in conteo_fumadores_por_genero.index else 0
cantidad_mujeres_fumadoras = conteo_fumadores_por_genero.loc[False, True] if False in conteo_fumadores_por_genero.index else 0

# Imprimir los resultados
print("\nCantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
