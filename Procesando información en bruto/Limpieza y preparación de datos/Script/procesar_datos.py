"""Parte 6: Automatizando el proceso
Imagina que los datos que procesaste en anteriores etapas del proyecto integrador se van actualizando cada cierto tiempo, (manteniendo el formato) y la url siempre va apuntando a la versión más actual, en este caso conviene tener automatizado el procesamiento en un script que pedas llamar y siempre te dé un csv limpio y listo para su análisis.

Tu tarea en esta etapa del proyecto consiste en crear un script (un archivo .py) que realice todas las operaciones vistas hasta ahora (desde el módulo de APIS) que al ejecutarse

Descargue los datos desde una url
Convierta todo a un dataframe
Categorice en grupos
Exporte un csv resultante
La url no debe estar definida como una constante en el código, en su lugar usa argumentos por terminal (revisar este enlace) para enviarle la url al programa al ejecutarlo."""

import requests
import pandas as pd
import numpy as np
url = 'URL_de_tu_dataset_actualizado'

def descargar_y_procesar_datos(url):
    try:
        # Realizar un GET request a la URL
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa

        # Escribir la respuesta en un archivo CSV
        with open('datos_descargados.csv', 'w') as archivo_csv:
            archivo_csv.write(response.text)

        print("Datos descargados y guardados en 'datos_descargados.csv'")

        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv('datos_descargados.csv')

        # Verificar valores faltantes, filas repetidas, eliminar valores atípicos y categorizar por edades
        procesar_dataframe(df)

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos: {e}")
    except Exception as e:
        print(f"Error al procesar el DataFrame: {e}")

def procesar_dataframe(df):
    # Verificar valores faltantes
    if df.isnull().values.any():
        print("Existen valores faltantes.")
        # Eliminar valores faltantes
        df = df.dropna()
        print("Valores faltantes eliminados.")

    # Verificar filas repetidas
    if df.duplicated().any():
        print("Existen filas repetidas.")
        # Eliminar filas repetidas
        df = df.drop_duplicates()
        print("Filas repetidas eliminadas.")

    # Verificar y eliminar valores atípicos
    # (Ajusta esta parte según la forma en que identificas y manejas los valores atípicos)

    # Crear columna que categorice por edades
    df['Categoria_Edad'] = pd.cut(df['age'], bins=[0, 12, 19, 39, 59, np.inf], labels=['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor'])

    # Guardar el resultado como CSV
    df.to_csv('datos_procesados.csv', index=False)
    print("Resultados guardados como 'datos_procesados.csv'.")

# Llamar a la función con la URL proporcionada
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
descargar_y_procesar_datos(url_datos)

