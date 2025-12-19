# Laboratorio N° 22_Ejercicio 04
# Autor: Andrea Camargo
# Colaboró:
# Tiempo: 15 minutos

import requests

params = {"limit": 10}
r = requests.get("https://pokeapi.co/api/v2/pokemon", params=params)
pokemons = r.json()["results"]

print("Primeros 10 Pokémon:")
for pokemon in pokemons:
    print(f"- {pokemon['name']}")