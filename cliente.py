import requests

url = 'http://172.17.38.44/enviar_numero'
data = {'numero': 42}

response = requests.post(url, json=data)
print(response.text)
