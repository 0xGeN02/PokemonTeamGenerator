from competitiveValueAlgorithm import calculate_competitiveValue
import json

with open('C:/Users/G513/University/2/ComplejidadComputacuional/PokemonTeamGenerator/data/pokemonStats.json', 'r') as file:
    pokemonStats = json.load(file)

for pokemon_name, pokemon_info in pokemonStats[1].items():
    competitive_value = calculate_competitiveValue(pokemon_info)
    print(f"{pokemon_name}: {competitive_value}")
