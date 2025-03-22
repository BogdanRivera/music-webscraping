import requests


ACCESS_TOKEN = "i5AoEUQHSNunEkNx0jMqrwwibgNZIOTg1k2LGO_Q_yWQGn8Jy2_HuBp9z5GUZJUd"

# Endpoint de búsqueda
url = "https://api.genius.com/search"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
params = {
    "q": "Adele"  # Término de búsqueda
}

# Realizar la solicitud
response = requests.get(url, headers=headers, params=params)

# Procesar la respuesta
if response.status_code == 200:
    data = response.json()
    for hit in data["response"]["hits"]:
        print(f"Título: {hit['result']['title']}, Artista: {hit['result']['primary_artist']['name']}")
else:
    print(f"Error: {response.status_code}")


