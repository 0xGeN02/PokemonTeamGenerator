from competitiveValue import calculate_competitiveValue
import json
import os

base_dir = os.path.dirname(__file__)
#Cargamos los datos de los json
def load_data(base_dir):
    with open(os.path.join(base_dir, '../data/pokemonData.json'), 'r') as file:
        pokemon_data = json.load(file)
    return pokemon_data

pokemon_data = load_data(base_dir)

#Funcion para calcular el peso de los pokemon en el json
def pokemonPesos(pokemon_data):
    array_pokemonPesos = []
    for pokemon_name, pokemon_info in pokemon_data[1].items():
        pokemon_competitiveValue = calculate_competitiveValue(pokemon_info)
        array_pokemonPesos.append([pokemon_name, pokemon_competitiveValue])
    return array_pokemonPesos

for pokemonPesado in pokemonPesos(pokemon_data):
    print(pokemonPesado)

#Funcion para clasificar los pokemon en arrays por tipo
jsonPokeByType = {}

def pokeByType(pokemon_data):
    for pokemon_name, pokemon_info in pokemon_data[1].items():
        for type in pokemon_info['type']:
            if type not in jsonPokeByType:
                jsonPokeByType[type] = []
            jsonPokeByType[type].append(pokemon_name)
    return jsonPokeByType

for type, pokemon in pokeByType(pokemon_data).items():
    print(type,':', pokemon)

def save_poekmonPesos(array_pokemonPesos, base_dir):
    data = {
        "pokemonPesos": array_pokemonPesos,
    }

    with open(os.path.join(base_dir, '../data/pokemonPesos.json'), 'w') as file:

        json.dump(data, file, indent=4)

def save_pokeByType(jsonPokeByType, base_dir):
    data = {
        "pokemonByType": jsonPokeByType,
    }

    with open(os.path.join(base_dir, '../data/pokemonByType.json'), 'w') as file:
        json.dump(data, file, indent=4)

save_poekmonPesos(pokemonPesos(pokemon_data), base_dir)
save_pokeByType(pokeByType(pokemon_data), base_dir)