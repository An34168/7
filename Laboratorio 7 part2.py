import requests
import json
api_key = "2e9b2351d24d4ff3aae006ff9e4587ac"
query = "Japan"

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&language=es&pageSize=5"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    if "articles" in data and len(data["articles"]) > 0:
        noticias = []
        for article in data["articles"][:5]:
            noticias.append({
                "Title": article["title"],
                "Source": article["source"]["name"],
                "Date": article["publishedAt"],
                "Description": article["description"],
                "URL": article["url"]
            })

        print("\n📰 **News about Japan** 🇯🇵\n")
        for i, noticia in enumerate(noticias, 1):
            print(f"🔹 {i}. {noticia['Title']}")
            print(f"   🏢 Source: {noticia['Source']}")
            print(f"   📅 Date: {noticia['Date']}")
            print(f"   📝 {noticia['Description']}")
            print(f"   🔗 More: {noticia['URL']}\n")
   
















