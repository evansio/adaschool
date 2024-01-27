import pandas as pd
from typing import Set

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    
    # Limpieza de datos demográficos
    data = data.drop(columns=['Race', 'Count', 'Number of Veterans'])
    data = data.drop_duplicates()
    
    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    import requests
    import json
    import sqlite3

    # Crear una tabla de dimensiones utilizando pandas para almacenar estos datos
    calidad_aire_data = {'city': [], 'CO': [], 'NO2': [], 'O3': [], 'SO2': [], 'PM2.5': [], 'PM10': [], 'overall_aqi': []}

    for ciudad in ciudades:
        # Obtener datos de calidad del aire de la API
        api_url = f"https://api-ninjas.com/api/airquality?city={ciudad}"
        response = requests.get(api_url)
        aire_data = json.loads(response.text)

        # Tomar el elemento concentration de cada entrada por fila
        calidad_aire_data['city'].append(ciudad)
        calidad_aire_data['CO'].append(aire_data['data']['concentration']['CO'])
        calidad_aire_data['NO2'].append(aire_data['data']['concentration']['NO2'])
        calidad_aire_data['O3'].append(aire_data['data']['concentration']['O3'])
        calidad_aire_data['SO2'].append(aire_data['data']['concentration']['SO2'])
        calidad_aire_data['PM2.5'].append(aire_data['data']['concentration']['PM2.5'])
        calidad_aire_data['PM10'].append(aire_data['data']['concentration']['PM10'])
        calidad_aire_data['overall_aqi'].append(aire_data['data']['concentration']['overall_aqi'])

    # Crear DataFrame
    ciudades_df = pd.DataFrame(calidad_aire_data)

    # Guardar el DataFrame en un archivo CSV
    ciudades_df.to_csv("ciudades.csv", index=False)

    # Crear base de datos SQLite y cargar las dos tablas procesadas
    conn = sqlite3.connect("demografia_aire.db")
    ej_1_cargar_datos_demograficos().to_sql("demografia", conn, index=False, if_exists="replace")
    ciudades_df.to_sql("calidad_aire", conn, index=False, if_exists="replace")
    conn.close()
