import requests

link = "https://www.google.com/search?q=palmeiras"

requisicao = requests.get(link)

print(requisicao.status_code)
print(requisicao.text)