# 1.Obtenemos todos los pokemons del json pokemonByType
# 2.Obtenemos las fortalezas y debilidades del equipo rival
# 3.Recalculamos el peso de los pokemon en relacion a las fortalezas y deblilodades del equipo rival 
#    nuevo valor del pokemon : puntoCombate = peso*(1+debilidades_rival)/(1+fortalezas_rival)
#     Por ejemplo el rival es fuerte conta agua y debil contra fuego
#     Si el peso del pokemon es 100 nuevo valor del pokemon si el pokemon es de tipo agua seria: 
#       puntoCombate = 100*(1+1)/(1+0) = 200
#     Si el peso del pokemon es 100 nuevo valor del pokemon si el pokemon es de tipo fuego seria:
#       puntoCombate = 100*(1+0)/(1+1) = 50
    
def get_puntosCombate(rivalData, pokePeso, pokeByType):

    # Obtenemos los pokemons del json pokemonByType
    pokemonsListed = pokeByType["pokemonByType"]
    # Por cada tipo dentro del array de weaknesses hemos de recorrer los pokemons y aumentar en +1 una variable nueva llamada ventaja_combate
    # Por cada tipo dentro del array de strengths hemos de recorrer los pokemons y disminuir en -1 una variable nueva llamada ventaja_combate
    # El valor de ventaja_combate nos dira si el pokemon es fuerte o debil contra el equipo rival

    # Obtenemos las fortalezas y debilidades del equipo rival
    rivalWeaknesses = rivalData['rivalWeaknesses']
    rivalStrengths = rivalData['rivalStrengths']

    # Recuperamos los pesos de cada uno de los pokemon
    pokePeso
    pokePeso_dict = {item[0]: item[1] for item in pokePeso["pokemonPesos"]}
    #Por cada valor del array rivalWeaknesses debemos aumentar un valor en relacion a un pokemon para recalcular el peso
    combatValue = {}
    for tipo, count in rivalWeaknesses.items():
        tipo = tipo.capitalize()
        # Por cada tipo dentro del array de weaknesses hemos de recorrer los pokemons y aumentar en +1 una variable nueva llamada ventaja_combate
        # el nuevo diccionario combat value guardara el pokemon y su valor de combate y su peso, la variable combate se multiplica por el counter asociado en el array de weaknesses
        # combatValue = { "pokemon": {"ventajaCombate": 0, "peso": 0}}
        for pokemon in pokemonsListed[tipo]:
            if pokemon not in pokePeso_dict:
                continue
            if pokemon not in combatValue:
                combatValue[pokemon] = {"ventajaCombate": 1*count/2, "desventajaCombate": 0, "peso": pokePeso_dict[pokemon]}
            else:
                combatValue[pokemon]["ventajaCombate"] += 1*count/2
    for tipo, count in rivalStrengths.items():
        tipo = tipo.capitalize()
        # Por cada tipo dentro del array de strengths hemos de recorrer los pokemons y disminuir en -1 una variable nueva llamada ventaja_combate
        # el nuevo diccionario combat value guardara el pokemon y su valor de combate y su peso, la variable combate se multiplica por el counter asociado en el array de strengths
        # combatValue = { "pokemon": {"desventajaCombate": 0, "peso": 0}}
        for pokemon in pokemonsListed[tipo]:
            if pokemon not in pokePeso_dict:
                continue
            if pokemon not in combatValue:
                combatValue[pokemon] = {"ventajaCombate": 0, "desventajaCombate": 1*count, "peso": pokePeso_dict[pokemon]}
            else:
                combatValue[pokemon]["desventajaCombate"] += 1*count
    # Recalculamos el peso de los pokemon en relacion a las fortalezas y deblilodades del equipo rival
    # nuevo valor del pokemon : puntoCombate = peso*(1+debilidades_rival)/(1+fortalezas_rival)
    for pokemon in combatValue:
        combatValue[pokemon]["puntosCombate"] = round(combatValue[pokemon]["peso"]*(1+0.5*combatValue[pokemon]["ventajaCombate"])/(1+0.5*combatValue[pokemon]["desventajaCombate"]),2)

    return combatValue

    
# 4.Ordenamos los pokemon por puntos de combate
# 5.Devolvemos los 6 primeros pokemons de la lista

def get_best_pokemon(puntosCombate):
    # Ordenamos los pokemon por puntos de combate
    sorted_pokemon = sorted(puntosCombate.items(), key=lambda x: x[1]["puntosCombate"], reverse=True)
    # Devolvemos los 6 primeros pokemons de la lista
    return sorted_pokemon[:6]


# 6.Obtenemos los datos asociados a los pokemons elegidos
def get_best_pokemon_info(best_team, pokeData):
    best_team_info = []
    for pokemon in best_team:
        pokemon_info = pokeData[1].get(pokemon[0], None)
        if pokemon_info is None:
            print("El pokemon " + pokemon + " no se encuentra en la base de datos")
            break
        pokemon_info['name'] = pokemon[0]
        best_team_info.append(pokemon_info)
    return best_team_info

# 7.Reestructuramos los datos para que sean mas faciles de leer por terminal
def print_pokemon_data(pokemon_info):
    print(f"{pokemon_info['name']}:")
    print("  Stats:")
    for stat, value in pokemon_info['stats'].items():
        print(f"    {stat.capitalize()}: {value}")
    print("  Moves:")
    for move, power in pokemon_info['moves'].items():
        print(f"    {move.capitalize()}: {power}")
    print(f"  Type: {', '.join(pokemon_info['type'])}")
    print(f"  Weaknesses: {', '.join(pokemon_info['weaknesses'])}")
    print(f"  Strengths: {', '.join(pokemon_info['strengths'])}")
    print(f"  Ability: {pokemon_info['ability']}")
    print(f"  EVs: {pokemon_info['evs']}")