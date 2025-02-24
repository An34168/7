import requests
import json
api_key = "2e9b2351d24d4ff3aae006ff9e4587ac"
query = "Japón"

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&language=es&pageSize=5"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    if "articles" in data and len(data["articles"]) > 0:
        noticias = []
        for article in data["articles"][:5]:
            noticias.append({
                "Título": article["title"],
                "Fuente": article["source"]["name"],
                "Fecha": article["publishedAt"],
                "Descripción": article["description"],
                "URL": article["url"]
            })

        print("\n📰 **Últimas Noticias sobre Japón** 🇯🇵\n")
        for i, noticia in enumerate(noticias, 1):
            print(f"🔹 {i}. {noticia['Título']}")
            print(f"   🏢 Fuente: {noticia['Fuente']}")
            print(f"   📅 Fecha: {noticia['Fecha']}")
            print(f"   📝 {noticia['Descripción']}")
            print(f"   🔗 Leer más: {noticia['URL']}\n")
   
















