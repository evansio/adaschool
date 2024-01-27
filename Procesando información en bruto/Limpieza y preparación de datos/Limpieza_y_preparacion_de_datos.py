"""Parte 5: Limpieza y preparación de datos
Una vez cargado el csv mediante el request anterior, realiza lo siguiente:

Verificar que no existan valores faltantes
Verificar que no existan filas repetidas
Verificar si existen valores atípicos y eliminarlos
Crear una columna que categorice por edades
0-12: Niño
13-19: Adolescente
20-39: Jóvenes adulto
40-59: Adulto
60-...: Adulto mayor
Guardar el resultado como csv
Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada."""

import pandas as pd
import numpy as np

def limpiar_y_preparar_datos(dataframe):
    try:
        # Verificar valores faltantes
        print(dataframe.isnull().sum())

        # Verificar filas repetidas
        print(dataframe.duplicated().sum())

        # Verificar y eliminar valores atípicos
        q1 = dataframe["age"].quantile(0.25)
        q3 = dataframe["age"].quantile(0.75)
        iqr = q3 - q1
        dataframe = dataframe[(dataframe["age"] >= q1 - 1.5 * iqr) & (dataframe["age"] <= q3 + 1.5 * iqr)]

        # Crear columna de categoría por edades
        bins = [0, 12, 19, 39, 59, float('inf')]
        labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
        dataframe['Categoria_Edad'] = pd.cut(dataframe['age'], bins=bins, labels=labels, right=False)

        # Guardar el resultado como CSV
        dataframe.to_csv('datos_limpios_variacion.csv', index=False)
        print("Datos limpios y preparados guardados en 'datos_limpios_variacion.csv'")
    except Exception as e:
        print(f"Error en la limpieza y preparación de datos: {e}")

# Cargar el archivo CSV descargado anteriormente
archivo_csv = 'datos_descargados.csv'
datos = pd.read_csv(archivo_csv)

# Llamar a la función con el DataFrame cargado
limpiar_y_preparar_datos(datos)
