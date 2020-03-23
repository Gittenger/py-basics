import requests
import json

print('welcome to the pokedex CLI.....')
pokemonName = input('Which Pokemon do you want to see? ')

data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonName}/')
if data.status_code == 200:
    data = json.loads(data.text)
    print(f"You chose {data['name']}")
    action = input(
        "What information would you like to see? \n(i=info, s=stats) ")
    # i = info, s = stats
    # info.... name, id, weight, height, types

    if action == "i" or action == "info":
        print(f"name: {data['name']}")
        print(f"id: {data['id']}")
        print(f"weight: {data['weight']}")
        print(f"height: {data['height']}")
        pokemon_type = ""
        for type in data['types']:
            if data['types'].index(type) == (len(data['types']) - 1):
                pokemon_type += f"{type['type']['name']}"
            else:
                pokemon_type += f"{type['type']['name']}, "
        print(f"types: {pokemon_type}")

    elif action == "s" or action == "stats":
        print(f"hp: {data['stats'][5]['base_stat']}")
        print(f"defense: {data['stats'][3]['base_stat']}")
        print(f"attack: {data['stats'][4]['base_stat']}")
        print(f"speed: {data['stats'][0]['base_stat']}")
        print(f"special defense: {data['stats'][1]['base_stat']}")
        print(f"special attack: {data['stats'][2]['base_stat']}")

    else:
        print('sorry we dont recognize that command')

else:
    print('Sorry thats not a valid pokemon')
