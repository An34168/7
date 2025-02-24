import requests
import json

# Tu API Key válida
api_key = "510fe9d0497256dc053c0e023afe5f5b"

# Pedir la ciudad (por defecto Quito si no ingresas nada)
city = "Saint Petersburg"



# Construcción de la URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar la respuesta antes de convertir a JSON
if response.status_code == 200:
    data = response.json()

    # Extraer la información relevante
    weather_info = {
        "Ciudad": data["name"],
        "Temperatura (°C)": data["main"]["temp"],
        "Sensación térmica (°C)": data["main"]["feels_like"],
        "Mínima (°C)": data["main"]["temp_min"],
        "Máxima (°C)": data["main"]["temp_max"],
        "Humedad (%)": data["main"]["humidity"],
        "Presión (hPa)": data["main"]["pressure"],
        "Descripción del clima": data["weather"][0]["description"]
    }

    # Imprimir los datos formateados
    print(json.dumps(weather_info, indent=4, ensure_ascii=False))
else:
    print(f"❌ Error: No se pudo obtener la información. Código de respuesta {response.status_code}")


