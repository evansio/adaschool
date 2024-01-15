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

# Calcular el promedio de edad
promedio_edad = np.mean(edades_np)

# Mostrar el resultado
print("El promedio de edad de las personas participantes en el estudio es:", promedio_edad)