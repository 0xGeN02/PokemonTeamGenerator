import json
import os

#cargamos los datos de los json
def load_data(base_dir):
    with open(os.path.join(base_dir, 'data/pokemonPesos.json'), 'r') as file:
        pokemon_peso = json.load(file)
    with open(os.path.join(base_dir, 'data/pokemonData.json'), 'r') as file:
        pokemon_data = json.load(file)
    with open(os.path.join(base_dir, 'data/pokemonTypeChart.json'), 'r') as file:
        pokemon_types = json.load(file)
    with open(os.path.join(base_dir, 'data/pokemonByType.json'), 'r') as file:
        pokemon_by_type = json.load(file)
    return pokemon_peso, pokemon_data, pokemon_types, pokemon_by_type

#Pedimos al user que introduzca los pokemon del rival o el equipo por defecto
def get_rival_team():
    rivalTeam = []
    default_rivalTeam = ['Charizard', 'Raichu', 'Gengar', 'Machamp', 'Gyarados', 'Alakazam']
    print("Pulse 0 si desea usar el equipo por defecto o 1 si desea introducir el equipo rival")
    option = int(input())
    if option == 0:
        rivalTeam = default_rivalTeam
    elif option == 1:
        print("Introduzca el equipo rival")
        for _ in range(6):
            pokemon = input()
            rivalTeam.append(pokemon)
    return rivalTeam

def get_rival_teamInfo(rivalTeam, pokemon_peso, pokemon_data, pokemon_types, pokemon_by_type):
    totalPeso = 0
    totalTypes = {}
    totalStrengths = {}
    totalWeaknesses = {}
    rival_pokemonInfo = {}
    rival_teamInfo = {}

    for pokemon in rivalTeam:
        # Encontramos el pokemon en pokemon_stats y en pokemon_pesos para obtener sus stats y su peso
        pokemonData = pokemon_data[1].get(pokemon, None)
        pokemonPeso = next((p[1] for p in pokemon_peso["pokemonPesos"] if p[0] == pokemon), None)
        if pokemonData is None or pokemonPeso is None:
            print("El pokemon " + pokemon + " no se encuentra en la base de datos")
            break
        # Calculamos el peso del pokemon y lo asignamos a la variable totalPeso
        peso = pokemonPeso
        totalPeso += peso
        
        # Obtenemos el array de tipos del pokemon y lo asignamos a la variable totalTypes
        tipo = pokemonData["type"]
        for type in tipo:
            if type in totalTypes:
                totalTypes[type] += 1
            else:
                totalTypes[type] = 1
        #Tras obtener el o los tipos del pokemon, guardamos en arrays sus fortalezas y debilidades relacionadas al tipo
        fortalezas = {}
        debilidades = {}

        # Por cada tipo del pokemon, obtenemos sus fortalezas y debilidades
        for type in tipo:
            for i in range(0, len(pokemon_types['type']), 2):
                if pokemon_types['type'][i].lower() == type.lower(): # Con el lower() nos aseguramos de que el tipo sea en minusculas y no haya problemas con mayusculas
                    typeAttributes = pokemon_types['type'][i+1]
                    for weakness in typeAttributes["weaknesses"]:
                        if weakness not in debilidades:
                            debilidades[weakness] = 1
                        else:
                            debilidades[weakness] += 1
                    for strength in typeAttributes["strengths"]:
                        if strength not in fortalezas:
                            fortalezas[strength] = 1
                        else:
                            fortalezas[strength] += 1

        #Añadimos las fortalezas y debilidades del pokemon a las variables totales
        for weakness in debilidades:
            if weakness in totalWeaknesses:
                totalWeaknesses[weakness] += debilidades[weakness]
            else:
                totalWeaknesses[weakness] = debilidades[weakness]
        for strength in fortalezas:
            if strength in totalStrengths:
                totalStrengths[strength] += fortalezas[strength]
            else:
                totalStrengths[strength] = fortalezas[strength]

        rival_pokemonInfo[pokemon] = {
            "Types": tipo,
            "Strengths": fortalezas,
            "Weaknesses": debilidades,
            "Peso": peso
        }

    rival_teamInfo = {
        "Total Types": totalTypes,
        "Total Strengths": totalStrengths,
        "Total Weaknesses": totalWeaknesses,
        "Total Peso": totalPeso
    }
    print(rival_teamInfo)

    return rival_pokemonInfo, rival_teamInfo
