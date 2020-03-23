import requests
import json

data = requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')
# convert to string, process using json.loads
# converts to be usable in python (dict)
data = json.loads(data.text)

print(data['moves'][0]['move']['name'])
