import requests
import json

api_key = "510fe9d0497256dc053c0e023afe5f5b"

city = "Saint Petersburg"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather_info = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Termic (°C)": data["main"]["feels_like"],
        "Minimum (°C)": data["main"]["temp_min"],
        "Max (°C)": data["main"]["temp_max"],
        "Huminity (%)": data["main"]["humidity"],
        "Pression (hPa)": data["main"]["pressure"],
        "Description of the weather": data["weather"][0]["description"]
    }
    print(json.dumps(weather_info, indent=4, ensure_ascii=False))
else:
    print(f"❌ Error {response.status_code}")


