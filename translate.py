import requests

res = requests.post("https://libretranslate.de/translate", data={
    "q": "Cześć, jak się masz?",
    "source": "pl",
    "target": "en",
    "format": "text"
}).json()

print(res)