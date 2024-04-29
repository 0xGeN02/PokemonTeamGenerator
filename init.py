import os
base_dir = os.path.dirname(__file__)
import sys
sys.path.append('..')
from scripts.rivalTeam import get_rival_team, get_rival_teamInfo, load_data
from lib.quicksortRivalAttributes import quickSort
from colorama import Fore
from scripts.yourTeam import get_puntosCombate, get_best_pokemon, get_best_pokemon_info, print_pokemon_data
from scripts.compareSorts import compareSorts

#start the program
print(Fore.YELLOW + str(""))
print("||||||||||||         ||||||||||||         ||||     ||||      |||||||||||       ||||||||           ||||||||       |||||||||||||       ||||||||       ||||")
print("||||    |||||      |||||||||||||||        ||||    ||||       ||||              |||| ||||        ||||  ||||      |||||||||||||||      |||| ||||      ||||")
print("||||     |||||     |||         |||        ||||   ||||        ||||              ||||  ||||      ||||   ||||      |||         |||      ||||  ||||     ||||")
print("||||    |||||      |||         |||        ||||  ||||         ||||              ||||   |||||  |||||    ||||      |||         |||      ||||   ||||    ||||")
print("||||||||||||       |||         |||        |||||||||          |||||||||||       ||||     ||||||||      ||||      |||         |||      ||||    ||||   ||||")
print("||||               |||         |||        ||||  ||||         ||||              ||||       ||||        ||||      |||         |||      ||||     ||||  ||||")
print("||||               |||         |||        ||||   ||||        ||||              ||||                   ||||      |||         |||      ||||      |||| ||||")
print("||||               |||||||||||||||        ||||    ||||       ||||              ||||                   ||||      |||||||||||||||      ||||       ||||||||")
print("||||                |||||||||||||         ||||     ||||      |||||||||||       ||||                   ||||       |||||||||||||       ||||         ||||||")
print(""+Fore.RESET)
print("Bienvenido a Pokemon Team Generator")
print("")

#Cargamos los datos de los json
(pokemon_peso, pokemon_data, pokemon_types, pokemon_byType) = load_data(base_dir)

#Pedimos al user que introduzca los pokemon del rival o el equipo por defecto
rivalTeam = get_rival_team()

#Obtenemos la informacion del equipo rival
(rivalTeamInfo, rivalPokemonInfo) = get_rival_teamInfo(rivalTeam, pokemon_peso, pokemon_data, pokemon_types)

#Reordenamos los valores de los diccionarios
reorderTypes = quickSort(rivalTeamInfo['totalTypes'])
reorderFrotalezas = quickSort(rivalTeamInfo['totalStrengths'])
reorderDebilidades = quickSort(rivalTeamInfo['totalWeaknesses'])
reorderedData = {'rivalTypes':reorderTypes, 'rivalStrengths': reorderFrotalezas, 'rivalWeaknesses': reorderDebilidades}

print("El equipo rival tiene un", Fore.MAGENTA + str("peso")+ Fore.RESET, "total de " + Fore.MAGENTA + str(rivalTeamInfo["totalPeso"])+ Fore.RESET)
print("")

print("Los", Fore.YELLOW + str("Pokemon")+ Fore.RESET, "del equipo rival son: ")
for pokemon in rivalTeam:
    print(pokemon)
print("")

print("Los tipos de", Fore.YELLOW + str("Pokemon")+ Fore.RESET, "que tiene el equipo rival son: ")
for type,count in reorderTypes.items():
    print(f"{type}: {count}")
print("")

print("Las", Fore.GREEN + str("fortalezas")+ Fore.RESET, "del equipo rival son: ")
for strengths, count in reorderFrotalezas.items():
    print(f"{strengths}: {count}")
print("")

print("Las", Fore.RED + str("debilidades")+ Fore.RESET, "del equipo rival son: ")
for weaknesses, count in reorderDebilidades.items():
    print(f"{weaknesses}: {count}")
print("")

(puntosCombate) = get_puntosCombate(reorderedData, pokemon_peso, pokemon_byType)
print("Los", Fore.CYAN + str("puntos de combate")+ Fore.RESET, "de los pokemons son: ")
for pokemon, value in puntosCombate.items():
    print(f"{pokemon}: {value['puntosCombate']}")
print("")

print("Comparando los algoritmos de ordenacion: ")
print("Selecciona el algoritmo de ordenacion que deseas utilizar: ")
print("1. Timsort Built-in Python")
print("2. Quicksort Algorithm")
print("3. Bubblesort Algorithm")
arg = int(input("Introduce el numero del algoritmo de ordenacion: "))

best_team = get_best_pokemon(puntosCombate, arg)
print("El equipo", Fore.LIGHTGREEN_EX + str("recomendado")+ Fore.RESET, "es: ")
for pokemon in best_team:
    print(pokemon[0])
print("")

compareSorts(puntosCombate)

best_team_info = get_best_pokemon_info(best_team, pokemon_data)
print(Fore.CYAN+"La informacion de los pokemons recomendados es: "+Fore.RESET)

#Print poke data
poke_colorScripts_dir = os.path.join(base_dir, 'git/pokemon-colorscripts')
for pokemon in best_team_info:
    print_pokemon_data(pokemon, poke_colorScripts_dir)

print(Fore.YELLOW+"Gracias por usar Pokemon Team Generator"+Fore.RESET)