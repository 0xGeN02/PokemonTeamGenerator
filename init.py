import os
base_dir = os.path.dirname(__file__)
import sys
sys.path.append('..')
from scripts.rivalTeam import get_rival_team, get_rival_teamInfo, load_data

#start the program
print("POKEMON TEAM GENERATOR")
print("|||||||||||\         ||||||||||||         ||||     ////      |||||||||||       ||||||||           |||||||||")
print("||||    ||||\      |||||||||||||||        ||||    ////       ||||              ||||  ||||        ||||  ||||")
print("||||     |||||     |||         |||        ||||   ////        ||||              ||||   ||||      ||||   ||||")
print("||||    ||||/      |||         |||        ||||  ////         ||||              ||||    |||||  |||||    ||||")
print("|||||||||||/       |||         |||        |||||||||          |||||||||||       ||||      ||||||||      ||||")
print("||||               |||         |||        ||||  \\\\         ||||              ||||        ||||        ||||")
print("||||               |||         |||        ||||   \\\\        ||||              ||||                    ||||")
print("||||               |||||||||||||||        ||||    \\\\       ||||              ||||                    ||||")
print("||||                |||||||||||||         ||||     \\\\      |||||||||||       ||||                    ||||")

(pokemon_peso, pokemon_stats, pokemon_types, pokemon_by_type) = load_data(base_dir)
rivalTeam = get_rival_team()
rivalTeamInfo = get_rival_teamInfo(rivalTeam, pokemon_peso, pokemon_stats, pokemon_types, pokemon_by_type)

