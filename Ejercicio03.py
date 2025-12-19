# Laboratorio N° 22_Ejercicio 03
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 10 minutos

import requests

url = "https://httpbin.org/get"
response = requests.get(url)
data = response.json()

print("IP de Origen:")
print(data["origin"])

print("\nHeaders:")
for key, value in data["headers"].items():
    print(f"{key} : {value}")

print("\nArgs (parámetros):")
print(data["args"])
