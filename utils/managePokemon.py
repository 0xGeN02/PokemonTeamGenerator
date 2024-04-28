from competitiveValue import calculate_competitiveValue
import json

with open('C:/Users/G513/University/2/ComplejidadComputacuional/PokemonTeamGenerator/data/pokemonData.json', 'r') as file:
    pokemon_stats = json.load(file)

#Funcion para calcular el peso de los pokemon en el json
def pokemonPesos():
    array_pokemonPesos = []
    for pokemon_name, pokemon_info in pokemon_stats[1].items():
        pokemon_competitiveValue = calculate_competitiveValue(pokemon_info)
        array_pokemonPesos.append([pokemon_name, pokemon_competitiveValue])
    return array_pokemonPesos

for pokemonPesado in pokemonPesos():
    print(pokemonPesado)

#Funcion para clasificar los pokemon en arrays por tipo
jsonPokeByType = {}

def pokeByType():
    for pokemon_name, pokemon_info in pokemon_stats[1].items():
        for type in pokemon_info['type']:
            if type not in jsonPokeByType:
                jsonPokeByType[type] = []
            jsonPokeByType[type].append(pokemon_name)
    return jsonPokeByType

for type, pokemon in pokeByType().items():
    print(type,':', pokemon)

def save_poekmonPesos(array_pokemonPesos):
    data = {
        "pokemonPesos": array_pokemonPesos,
    }

    with open('C:/Users/G513/University/2/ComplejidadComputacuional/PokemonTeamGenerator/data/pokemonPesos.json', 'w') as file:
        json.dump(data, file, indent=4)

def save_pokeByType(jsonPokeByType):
    data = {
        "pokemonByType": jsonPokeByType,
    }

    with open('C:/Users/G513/University/2/ComplejidadComputacuional/PokemonTeamGenerator/data/pokemonByType.json', 'w') as file:

        json.dump(data, file, indent=4)

save_poekmonPesos(pokemonPesos())
save_pokeByType(pokeByType())