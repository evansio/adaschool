import requests

def descargar_datos_csv(url):
    try:
        # Realizar un GET request a la URL
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa

        # Escribir la respuesta en un archivo CSV
        with open('datos_descargados.csv', 'w') as archivo_csv:
            archivo_csv.write(response.text)

        print("Datos descargados y guardados en 'datos_descargados.csv'")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos: {e}")

# Llamar a la función con la URL proporcionada
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
descargar_datos_csv(url_datos)
