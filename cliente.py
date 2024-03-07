import requests

url = 'http://192.168.0.163/enviar_numero'
data = {'numero': 42}

response = requests.post(url, json=data)
print(response.text)


