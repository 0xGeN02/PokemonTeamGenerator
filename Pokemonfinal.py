import random

class Pokemon:
    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
        
    def __repr__(self):
        # Esta función controla cómo se muestra el objeto cuando lo imprimes
        return f"{self.nombre}"


bulbasaur = Pokemon(nombre="Bulbasaur", tipo="Planta",peso= 1)
ivysaur = Pokemon(nombre="Ivysaur", tipo = "Planta", peso = 2)
venusaur = Pokemon(nombre="Venusaur", tipo = "Planta", peso = 3)
charmander = Pokemon(nombre="Charmander", tipo = "Fuego", peso = 4)
charmeleon = Pokemon(nombre="Charmeleon", tipo = "Fuego", peso = 5)
charizard = Pokemon(nombre="Charizard", tipo="Fuego", peso=6)
squirtle = Pokemon(nombre="Squirtle", tipo="Agua", peso=7)
wartortle = Pokemon(nombre="Wartortle", tipo="Agua", peso=8)
blastoise = Pokemon(nombre="Blastoise", tipo="Agua", peso=9)
caterpie = Pokemon(nombre="Caterpie", tipo="Bicho", peso=10)
metapod = Pokemon(nombre="Metapod", tipo="Bicho", peso=11)
butterfree = Pokemon(nombre="Butterfree", tipo="Bicho", peso=12)
weedle = Pokemon(nombre="Weedle", tipo="Bicho", peso=13)
kakuna = Pokemon(nombre="Kakuna", tipo="Bicho", peso=14)
beedrill = Pokemon(nombre="Beedrill", tipo="Bicho", peso=15)
pidgey = Pokemon(nombre="Pidgey", tipo="Normal", peso=16)
pidgeotto = Pokemon(nombre="Pidgeotto", tipo="Volador", peso=17)
pidgeot = Pokemon(nombre="Pidgeot", tipo="Volador", peso=18)
rattata = Pokemon(nombre="Rattata", tipo="Normal", peso=19)
raticate = Pokemon(nombre="Raticate", tipo="Normal", peso=20)
spearow = Pokemon(nombre="Spearow", tipo="Normal", peso=21)
fearow = Pokemon(nombre="Fearow", tipo="Volador", peso=22)
ekans = Pokemon(nombre="Ekans", tipo="Veneno", peso=23)
arbok = Pokemon(nombre="Arbok", tipo="Veneno", peso=24)
pikachu = Pokemon(nombre="Pikachu", tipo="Electrico", peso=25)
raichu = Pokemon(nombre="Raichu", tipo="Electrico", peso=26)
sandshrew = Pokemon(nombre="Sandshrew", tipo="Tierra", peso=27)
sandslash = Pokemon(nombre="Sandslash", tipo="Tierra", peso=28)
nidoran_f = Pokemon(nombre="Nidoran♀", tipo="Veneno", peso=29)
nidorina = Pokemon(nombre="Nidorina", tipo="Veneno", peso=30)
nidoqueen = Pokemon(nombre="Nidoqueen", tipo="Veneno", peso=31)
nidoran_m = Pokemon(nombre="Nidoran♂", tipo="Veneno", peso=32)
nidorino = Pokemon(nombre="Nidorino", tipo="Veneno", peso=33)
nidoking = Pokemon(nombre="Nidoking", tipo="Veneno", peso=34)
clefairy = Pokemon(nombre="Clefairy", tipo="Hada", peso=35)
clefable = Pokemon(nombre="Clefable", tipo="Hada", peso=36)
vulpix = Pokemon(nombre="Vulpix", tipo="Fuego", peso=37)
ninetales = Pokemon(nombre="Ninetales", tipo="Fuego", peso=38)
jigglypuff = Pokemon(nombre="Jigglypuff", tipo="Normal", peso=39)
wigglytuff = Pokemon(nombre="Wigglytuff", tipo="Normal", peso=40)
zubat = Pokemon(nombre="Zubat", tipo="Veneno", peso=41)
golbat = Pokemon(nombre="Golbat", tipo="Veneno", peso=42)
oddish = Pokemon(nombre="Oddish", tipo="Planta", peso=43)
gloom = Pokemon(nombre="Gloom", tipo="Planta", peso=44)
vileplume = Pokemon(nombre="Vileplume", tipo="Planta", peso=45)
paras = Pokemon(nombre="Paras", tipo="Bicho", peso=46)
parasect = Pokemon(nombre="Parasect", tipo="Bicho", peso=47)
venonat = Pokemon(nombre="Venonat", tipo="Bicho", peso=48)
venomoth = Pokemon(nombre="Venomoth", tipo="Bicho", peso=49)
diglett = Pokemon(nombre="Diglett", tipo="Tierra", peso=50)
dugtrio = Pokemon(nombre="Dugtrio", tipo="Tierra", peso=51)
meowth = Pokemon(nombre="Meowth", tipo="Normal", peso=52)
persian = Pokemon(nombre="Persian", tipo="Normal", peso=53)
psyduck = Pokemon(nombre="Psyduck", tipo="Agua", peso=54)
golduck = Pokemon(nombre="Golduck", tipo="Agua", peso=55)
mankey = Pokemon(nombre="Mankey", tipo="Lucha", peso=56)
primeape = Pokemon(nombre="Primeape", tipo="Lucha", peso=57)
growlithe = Pokemon(nombre="Growlithe", tipo="Fuego", peso=58)
arcanine = Pokemon(nombre="Arcanine", tipo="Fuego", peso=59)
poliwag = Pokemon(nombre="Poliwag", tipo="Agua", peso=60)
poliwhirl = Pokemon(nombre="Poliwhirl", tipo="Agua", peso=61)
poliwrath = Pokemon(nombre="Poliwrath", tipo="Agua", peso=62)
abra = Pokemon(nombre="Abra", tipo="Psiquico", peso=63)
kadabra = Pokemon(nombre="Kadabra", tipo="Psiquico", peso=64)
alakazam = Pokemon(nombre="Alakazam", tipo="Psiquico", peso=65)
machop = Pokemon(nombre="Machop", tipo="Lucha", peso=66)
machoke = Pokemon(nombre="Machoke", tipo="Lucha", peso=67)
machamp = Pokemon(nombre="Machamp", tipo="Lucha", peso=68)
bellsprout = Pokemon(nombre="Bellsprout", tipo="Planta", peso=69)
weepinbell = Pokemon(nombre="Weepinbell", tipo="Planta", peso=70)
victreebel = Pokemon(nombre="Victreebel", tipo="Planta", peso=71)
tentacool = Pokemon(nombre="Tentacool", tipo="Agua", peso=72)
tentacruel = Pokemon(nombre="Tentacruel", tipo="Agua", peso=73)
geodude = Pokemon(nombre="Geodude", tipo="Roca", peso=74)
graveler = Pokemon(nombre="Graveler", tipo="Roca", peso=75)
golem = Pokemon(nombre="Golem", tipo="Roca", peso=76)
ponyta = Pokemon(nombre="Ponyta", tipo="Fuego", peso=77)
rapidash = Pokemon(nombre="Rapidash", tipo="Fuego", peso=78)
slowpoke = Pokemon(nombre="Slowpoke", tipo="Agua", peso=79)
slowbro = Pokemon(nombre="Slowbro", tipo="Agua", peso=80)
magnemite = Pokemon(nombre="Magnemite", tipo="Electrico", peso=81)
magneton = Pokemon(nombre="Magneton", tipo="Electrico", peso=82)
farfetchd = Pokemon(nombre="Farfetch'd", tipo="Normal", peso=83)
doduo = Pokemon(nombre="Doduo", tipo="Normal", peso=84)
dodrio = Pokemon(nombre="Dodrio", tipo="Normal", peso=85)
seel = Pokemon(nombre="Seel", tipo="Agua", peso=86)
dewgong = Pokemon(nombre="Dewgong", tipo="Agua", peso=87)
grimer = Pokemon(nombre="Grimer", tipo="Veneno", peso=88)
muk = Pokemon(nombre="Muk", tipo="Veneno", peso=89)
shellder = Pokemon(nombre="Shellder", tipo="Agua", peso=90)
cloyster = Pokemon(nombre="Cloyster", tipo="Agua", peso=91)
gastly = Pokemon(nombre="Gastly", tipo="Fantasma", peso=92)
haunter = Pokemon(nombre="Haunter", tipo="Fantasma", peso=93)
gengar = Pokemon(nombre="Gengar", tipo="Fantasma", peso=94)
onix = Pokemon(nombre="Onix", tipo="Roca", peso=95)
drowzee = Pokemon(nombre="Drowzee", tipo="Psiquico", peso=96)
hypno = Pokemon(nombre="Hypno", tipo="Psiquico", peso=97)
krabby = Pokemon(nombre="Krabby", tipo="Agua", peso=98)
kingler = Pokemon(nombre="Kingler", tipo="Agua", peso=99)
voltorb = Pokemon(nombre="Voltorb", tipo="Electrico", peso=100)
electrode = Pokemon(nombre="Electrode", tipo="Electrico", peso=101)
exeggcute = Pokemon(nombre="Exeggcute", tipo="Planta", peso=102)
exeggutor = Pokemon(nombre="Exeggutor", tipo="Planta", peso=103)
cubone = Pokemon(nombre="Cubone", tipo="Tierra", peso=104)
marowak = Pokemon(nombre="Marowak", tipo="Tierra", peso=105)
hitmonlee = Pokemon(nombre="Hitmonlee", tipo="Lucha", peso=106)
hitmonchan = Pokemon(nombre="Hitmonchan", tipo="Lucha", peso=107)
lickitung = Pokemon(nombre="Lickitung", tipo="Normal", peso=108)
koffing = Pokemon(nombre="Koffing", tipo="Veneno", peso=109)
weezing = Pokemon(nombre="Weezing", tipo="Veneno", peso=110)
rhyhorn = Pokemon(nombre="Rhyhorn", tipo="Tierra", peso=111)
rhydon = Pokemon(nombre="Rhydon", tipo="Tierra", peso=112)
chansey = Pokemon(nombre="Chansey", tipo="Normal", peso=113)
tangela = Pokemon(nombre="Tangela", tipo="Planta", peso=114)
kangaskhan = Pokemon(nombre="Kangaskhan", tipo="Normal", peso=115)
horsea = Pokemon(nombre="Horsea", tipo="Agua", peso=116)
seadra = Pokemon(nombre="Seadra", tipo="Agua", peso=117)
goldeen = Pokemon(nombre="Goldeen", tipo="Agua", peso=118)
seaking = Pokemon(nombre="Seaking", tipo="Agua", peso=119)
staryu = Pokemon(nombre="Staryu", tipo="Agua", peso=120)
starmie = Pokemon(nombre="Starmie", tipo="Agua", peso=121)
mr_mime = Pokemon(nombre="Mr. Mime", tipo="Psiquico", peso=122)
scyther = Pokemon(nombre="Scyther", tipo="Bicho", peso=123)
jynx = Pokemon(nombre="Jynx", tipo="Hielo", peso=124)
electabuzz = Pokemon(nombre="Electabuzz", tipo="Electrico", peso=125)
magmar = Pokemon(nombre="Magmar", tipo="Fuego", peso=126)
pinsir = Pokemon(nombre="Pinsir", tipo="Bicho", peso=127)
tauros = Pokemon(nombre="Tauros", tipo="Normal", peso=128)
magikarp = Pokemon(nombre="Magikarp", tipo="Agua", peso=129)
gyarados = Pokemon(nombre="Gyarados", tipo="Agua", peso=130)
lapras = Pokemon(nombre="Lapras", tipo="Agua", peso=131)
ditto = Pokemon(nombre="Ditto", tipo="Normal", peso=132)
eevee = Pokemon(nombre="Eevee", tipo="Normal", peso=133)
vaporeon = Pokemon(nombre="Vaporeon", tipo="Agua", peso=134)
jolteon = Pokemon(nombre="Jolteon", tipo="Electrico", peso=135)
flareon = Pokemon(nombre="Flareon", tipo="Fuego", peso=136)
porygon = Pokemon(nombre="Porygon", tipo="Normal", peso=137)
omanyte = Pokemon(nombre="Omanyte", tipo="Roca", peso=138)
omastar = Pokemon(nombre="Omastar", tipo="Roca", peso=139)
kabuto = Pokemon(nombre="Kabuto", tipo="Roca", peso=140)
kabutops = Pokemon(nombre="Kabutops", tipo="Roca", peso=141)
aerodactyl = Pokemon(nombre="Aerodactyl", tipo="Roca", peso=142)
snorlax = Pokemon(nombre="Snorlax", tipo="Normal", peso=143)
articuno = Pokemon(nombre="Articuno", tipo="Hielo", peso=144)
zapdos = Pokemon(nombre="Zapdos", tipo="Electrico", peso=145)
moltres = Pokemon(nombre="Moltres", tipo="Fuego", peso=146)
dratini = Pokemon(nombre="Dratini", tipo="Dragon", peso=147)
dragonair = Pokemon(nombre="Dragonair", tipo="Dragon", peso=148)
dragonite = Pokemon(nombre="Dragonite", tipo="Dragon", peso=149)
mewtwo = Pokemon(nombre="Mewtwo", tipo="Psiquico", peso=150)
mew = Pokemon(nombre="Mew", tipo="Psiquico", peso=151)

pokemons = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot, rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoran_f, nidorina, nidoqueen, nidoran_m, nidorino, nidoking, clefairy, clefable, vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape, growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler, golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel, dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno, krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra, goldeen, seaking, staryu, starmie, mr_mime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyarados, lapras, ditto, eevee, vaporeon, jolteon, flareon, porygon, omanyte, omastar, kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]


#USAR ESTOS CUANDO SE MIRA LOS TIPOS QUE YA ESTAN EN EL EQUIPO CUANDO SE REEMPLAZA, NO USAr LOS TEMPS.
tipos = {
    'Bicho': 0,
    'Dragon': 0,
    'Electrico': 0,
    'Lucha': 0,
    'Fuego': 0,
    'Volador': 0,
    'Fantasma': 0,
    'Planta': 0,
    'Tierra': 0,
    'Hielo': 0,
    'Normal': 0,
    'Veneno': 0,
    'Psiquico': 0,
    'Roca': 0,
    'Agua': 0
}


Temp_Bichos=0
Temp_Dragones=0
Temp_Electricos=0
Temp_Luchas=0
Temp_Fuegos=0
Temp_Voladores=0
Temp_Fantasmas=0
Temp_Plantas=0
Temp_Tierras=0
Temp_Hielos=0
Temp_Normales=0
Temp_Venenos=0
Temp_Psiquicos=0
Temp_Rocas=0
Temp_Aguas=0




def solicitar_equipo_usuario():
    Equipo = []
    for i in range(6):
        nombre_pokemon = input(f"Introduce el nombre del Pokémon {i+1}: ")# poner en minusculas no mayusculas o no va
        Equipo.append(eval(nombre_pokemon))  # Utiliza eval para convertir el nombre en un objeto
    return Equipo

# Equipo por defecto
Equipo_defecto = [venonat, venomoth, squirtle, ivysaur, charmeleon, wartortle]

respuesta = input("Introduce 0 para usar el Equipo por defecto, o 1 para crear uno personalizado: ")

if respuesta == '0':
    Equipo = Equipo_defecto
elif respuesta == '1':
    Equipo = solicitar_equipo_usuario()
else:
    print("Respuesta no válida. Usando Equipo por defecto.")
    Equipo = Equipo_defecto

# Muestra la lista de Pokémon
print("Equipo:", Equipo)



for pokemon in Equipo:
    if pokemon.tipo == "Bicho":
        tipos['Bicho'] +=1
    elif pokemon.tipo == "Dragon":
        tipos['Dragon'] +=1
    elif pokemon.tipo == "Electrico":
        tipos['Electrico'] +=1
    elif pokemon.tipo == "Lucha":
        tipos['Lucha'] +=1
    elif pokemon.tipo == "Fuego":
        tipos['Fuego'] +=1
    elif pokemon.tipo == "Volador":
        tipos['Volador'] +=1
    elif pokemon.tipo == "Fantasma":
        tipos['Fantasma'] +=1
    elif pokemon.tipo == "Planta":
        tipos['Planta'] +=1
    elif pokemon.tipo == "Tierra":
        tipos['Tierra'] +=1
    elif pokemon.tipo == "Hielo":
        tipos['Hielo'] +=1
    elif pokemon.tipo == "Normal":
        tipos['Normal'] +=1
    elif pokemon.tipo == "Veneno":
        tipos['Veneno'] +=1
    elif pokemon.tipo == "Psiquico":
        tipos['Psiquico'] +=1
    elif pokemon.tipo == "Roca":
        tipos['Roca'] +=1
    elif pokemon.tipo == "Agua":
        tipos['Agua'] +=1

# Filtrar tipos que tienen valor 0

def obtener_pokemon_aleatorio(tipo):
    # Filtrar Pokémon del tipo deseado
    pokemons_filtrados = [pokemon for pokemon in pokemons if pokemon.tipo == tipo]
    # Si no hay Pokémon de ese tipo, retornar None
    if not pokemons_filtrados:
        return None
    # Usar el peso como probabilidad
    pesos = [pokemon.peso for pokemon in pokemons_filtrados]
    pokemon_seleccionado = random.choices(pokemons_filtrados, weights=pesos, k=1)[0]
    return pokemon_seleccionado


#ESTE IF INICIAL ES PARA QUE NO TENGA QUE HACER TODAS LAS VERIFICACIONES DE AQUI PARA ABAJO SI EL EQUIPO YA ES VALIDO
#AQUI ANTES SI NO FUNCIONA CUANDO HAY MAS DE DOS DEL MISMO TIPO PROBAR A PONER UN BUCLE, SI SIGUE SIN IR, SE DEJA COMO ESTABA
if tipos['Bicho'] >= 2 or tipos['Dragon'] >= 2 or tipos['Electrico'] >= 2 or tipos['Lucha'] >= 2 or tipos['Fuego'] >= 2 or tipos['Volador'] >= 2 or tipos['Fantasma'] >= 2 or tipos['Planta'] >= 2 or tipos['Tierra'] >= 2 or tipos['Hielo'] >= 2 or tipos['Normal'] >= 2 or tipos['Veneno'] >= 2 or tipos['Psiquico'] >= 2 or tipos['Roca'] >= 2 or tipos['Agua'] >= 2:
    print("Tienes al menos dos Pokémon con el mismo tipo.")
    if tipos['Bicho'] >= 2:
        Temp_Bichos=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Bicho":
                Temp_Bichos +=1
        if Temp_Bichos <=1:
            print("Tipo bicho repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI BICHO NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Bichos >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo,.
            Temp_Bichos=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Bicho":
                    Temp_Bichos +=1
            if Temp_Bichos <=1:
                print("Tipo bicho repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI BICHO NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon  
            elif Temp_Bichos >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Bichos=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Bicho":
                        Temp_Bichos +=1
                if Temp_Bichos <=1:
                    print("Tipo bicho repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI BICHO NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon  
                elif Temp_Bichos >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Bichos=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Bicho":
                            Temp_Bichos +=1
                    if Temp_Bichos <=1:
                        print("Tipo bicho repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI BICHO NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon  
                    elif Temp_Bichos >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo bicho repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon  
    if tipos['Dragon'] >= 2:
        Temp_Dragones=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Dragon":
                Temp_Dragones +=1
        if Temp_Dragones <=1:
            print("Tipo dragon repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI DRAGON NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Dragones >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo,.
            Temp_Dragones=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Dragon":
                    Temp_Dragones +=1
            if Temp_Dragones <=1:
                print("Tipo dragon repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI DRAGON NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Dragones >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Dragones=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Dragon":
                        Temp_Dragones +=1
                if Temp_Dragones <=1:
                    print("Tipo dragon repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI DRAGON NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Dragones >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Dragones=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Dragon":
                            Temp_Dragones +=1
                    if Temp_Dragones <=1:
                        print("Tipo dragon repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI Dragon NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Dragones >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo dragon repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon 
                        
    if tipos['Electrico'] >= 2:
        Temp_Electricos=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Electrico":
                Temp_Electricos +=1
        if Temp_Electricos <=1:
            print("Tipo electrico repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ELECTRICO NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Electricos >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Electricos=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Electrico":
                    Temp_Electricos +=1
            if Temp_Electricos <=1:
                print("Tipo electrico repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ELECTRICO NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Electricos >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Electricos=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Electrico":
                        Temp_Electricos +=1
                if Temp_Electricos <=1:
                    print("Tipo electrico repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI Electrico NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Electricos >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Electricos=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Electrico":
                            Temp_Electricos +=1
                    if Temp_Electricos <=1:
                        print("Tipo electrico repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ELECTRICO NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Electricos >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo electrico repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon
                        
    if tipos['Lucha'] >= 2:
        Temp_Luchas=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Lucha":
                Temp_Luchas +=1
        if Temp_Luchas <=1:
            print("Tipo lucha repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI Lucha NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Luchas >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo,.
            Temp_Luchas=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Lucha":
                    Temp_Luchas +=1
            if Temp_Luchas <=1:
                print("Tipo lucha repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI LUCHA NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Luchas >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Luchas=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Lucha":
                        Temp_Luchas +=1
                if Temp_Luchas <=1:
                    print("Tipo lucha repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI LUCHA NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Luchas >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Luchas=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Lucha":
                            Temp_Luchas +=1
                    if Temp_Luchas <=1:
                        print("Tipo lucha repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI LUCHA NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Luchas >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo lucha repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Fuego'] >= 2:
        Temp_Fuegos=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Fuego":
                Temp_Fuegos +=1
        if Temp_Fuegos <=1:
            print("Tipo fuego repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FUEGO NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Fuegos >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo,.
            Temp_Fuegos=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Fuego":
                    Temp_Fuegos +=1
            if Temp_Fuegos <=1:
                print("Tipo fuego repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FUEGO NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Fuegos >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Fuegos=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Fuego":
                        Temp_Fuegos +=1
                if Temp_Fuegos <=1:
                    print("Tipo fuego repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FUEGO NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Fuegos >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Fuegos=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Fuego":
                            Temp_Fuegos +=1
                    if Temp_Fuegos <=1:
                        print("Tipo fuego repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FUEGO NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Fuegos >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo fuego repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Volador'] >= 2:
        Temp_Voladores=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Volador":
                Temp_Voladores +=1
        if Temp_Voladores <=1:
            print("Tipo volador repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VOLADOR NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Voladores >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo,.
            Temp_Voladores=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Volador":
                    Temp_Voladores +=1
            if Temp_Voladores <=1:
                print("Tipo volador repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VOLADOR NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Voladores >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Voladores=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Volador":
                        Temp_Voladores +=1
                if Temp_Voladores <=1:
                    print("Tipo volador repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VOLADOR NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Voladores >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Voladores=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Volador":
                            Temp_Voladores +=1
                    if Temp_Voladores <=1:
                        print("Tipo volador repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VOLADOR NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Voladores >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo volador repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Fantasma'] >= 2:
        Temp_Fantasmas=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Fantasma":
                Temp_Fantasmas +=1
        if Temp_Fantasmas <=1:
            print("Tipo fantasma repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FANTASMA NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Fantasmas >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Fantasmas=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Fantasma":
                    Temp_Fantasmas +=1
            if Temp_Fantasmas <=1:
                print("Tipo fantasma repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FANTASMA NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Fantasmas >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Fantasmas=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Fantasma":
                        Temp_Fantasmas +=1
                if Temp_Fantasmas <=1:
                    print("Tipo fantasma repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FANTASMA NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Fantasmas >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Fantasmas=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Fantasma":
                            Temp_Fantasmas +=1
                    if Temp_Fantasmas <=1:
                        print("Tipo fantasma repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI FANTASMA NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Fantasmas >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo fantasma repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Planta'] >= 2:
        Temp_Plantas=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Planta":
                Temp_Plantas +=1
        if Temp_Plantas <=1:
            print("Tipo planta repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PLANTA NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Plantas >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Plantas=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Planta":
                    Temp_Plantas +=1
            if Temp_Plantas <=1:
                print("Tipo planta repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PLANTA NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Plantas >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Plantas=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Planta":
                        Temp_Plantas +=1
                if Temp_Plantas <=1:
                    print("Tipo planta repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PLANTA NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Plantas >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Plantas=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Planta":
                            Temp_Plantas +=1
                    if Temp_Plantas <=1:
                        print("Tipo planta repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PLANTA NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Plantas >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo planta repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Tierra'] >= 2:
        Temp_Tierras=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Tierra":
                Temp_Tierras +=1
        if Temp_Tierras <=1:
            print("Tipo tierra repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI TIERRA NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Tierras >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Tierras=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Tierra":
                    Temp_Tierras +=1
            if Temp_Tierras <=1:
                print("Tipo tierra repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI TIERRA NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Tierras >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Tierras=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Tierra":
                        Temp_Tierras +=1
                if Temp_Tierras <=1:
                    print("Tipo tierra repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI TIERRA NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Tierras >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Tierras=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Tierra":
                            Temp_Tierras +=1
                    if Temp_Tierras <=1:
                        print("Tipo tierra repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI TIERRA NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Tierras >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo tierra repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Hielo'] >= 2:
        Temp_Hielos=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Hielo":
                Temp_Hielos +=1
        if Temp_Hielos <=1:
            print("Tipo hielo repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI HIELO NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Hielos >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Hielos=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Hielo":
                    Temp_Hielos +=1
            if Temp_Hielos <=1:
                print("Tipo hielo repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI HIELO NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Hielos >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Hielos=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Hielo":
                        Temp_Hielos +=1
                if Temp_Hielos <=1:
                    print("Tipo hielo repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI HIELO NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Hielos >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Hielos=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Hielo":
                            Temp_Hielos +=1
                    if Temp_Hielos <=1:
                        print("Tipo hielo repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI HIELO NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Hielos >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo hielo repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Normal'] >= 2:
        Temp_Normales=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Normal":
                Temp_Normales +=1
        if Temp_Normales <=1:
            print("Tipo normal repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI NORMAL NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Normales >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Normales=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Normal":
                    Temp_Normales +=1
            if Temp_Normales <=1:
                print("Tipo normal repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI NORMAL NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Normales >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Normales=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Normal":
                        Temp_Normales +=1
                if Temp_Normales <=1:
                    print("Tipo normal repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI NORMAL NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Normales >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Normales=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Normal":
                            Temp_Normales +=1
                    if Temp_Normales <=1:
                        print("Tipo normal repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI NORMAL NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Normales >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo normal repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Veneno'] >= 2:
        Temp_Venenos=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Veneno":
                Temp_Venenos +=1
        if Temp_Venenos <=1:
            print("Tipo veneno repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VEVENO NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Venenos >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Venenos=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Veneno":
                    Temp_Venenos +=1
            if Temp_Venenos <=1:
                print("Tipo veneno repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VENENO NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Venenos >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Venenos=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Veneno":
                        Temp_Venenos +=1
                if Temp_Venenos <=1:
                    print("Tipo veneno repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VENENO NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Venenos >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Venenos=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Veneno":
                            Temp_Venenos +=1
                    if Temp_Venenos <=1:
                        print("Tipo veneno repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI VENENO NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Venenos >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo veneno repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Psiquico'] >= 2:
        Temp_Psiquicos=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Psiquico":
                Temp_Psiquicos +=1
        if Temp_Psiquicos <=1:
            print("Tipo psiquico repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PSIQUICO NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Psiquicos >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Psiquicos=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Psiquico":
                    Temp_Psiquicos +=1
            if Temp_Psiquicos <=1:
                print("Tipo psiquico repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PSIQUICO NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Psiquicos >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Psiquicos=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Psiquico":
                        Temp_Psiquicos +=1
                if Temp_Psiquicos <=1:
                    print("Tipo psiquico repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PSIQUICO NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Psiquicos >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Psiquicos=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Psiquico":
                            Temp_Psiquicos +=1
                    if Temp_Psiquicos <=1:
                        print("Tipo psiquico repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI PSIQUICO NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Psiquicos >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo psiquico repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Roca'] >= 2:
        Temp_Rocas=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Roca":
                Temp_Rocas +=1
        if Temp_Rocas <=1:
            print("Tipo roca repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ROCA NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Rocas >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Rocas=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Roca":
                    Temp_Rocas +=1
            if Temp_Rocas <=1:
                print("Tipo roca repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ROCA NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Rocas >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Rocas=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Roca":
                        Temp_Rocas +=1
                if Temp_Rocas <=1:
                    print("Tipo roca repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ROCA NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Rocas >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Rocas=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Roca":
                            Temp_Rocas +=1
                    if Temp_Rocas <=1:
                        print("Tipo roca repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI ROCA NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Rocas >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo roca repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon

    if tipos['Agua'] >= 2:
        Temp_Aguas=0
        for pokemon in Equipo[:5]:
            #Recuenta hasta la quinta posicion
            if pokemon.tipo == "Agua":
                Temp_Aguas +=1
        if Temp_Aguas <=1:
            print("Tipo agua repetido ere el sexto, cambiar posicion 6")
            #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI AGUA NI DE LOS Q YA HAY
            tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
            tipo_seleccionado = random.choice(tipos_con_valor_cero)
            tipos[tipo_seleccionado] +=1
            nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
            Equipo[5] = nuevo_pokemon 
        elif Temp_Aguas >=2:
            #Si el ultimo no era el repetido, se hace hasta encontrarlo.
            Temp_Aguas=0
            for pokemon in Equipo[:4]:
                #Mirar si hasta el cuarto hay repetidos
                if pokemon.tipo == "Agua":
                    Temp_Aguas +=1
            if Temp_Aguas <=1:
                print("Tipo agua repetido ere el quinto, cambiar posicion 5")
                #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI AGUA NI DE LOS Q YA HAY
                tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                tipo_seleccionado = random.choice(tipos_con_valor_cero)
                tipos[tipo_seleccionado] +=1
                nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                Equipo[4] = nuevo_pokemon
            elif Temp_Aguas >=2:
                #Si el quinto no era el repetido, se hace hasta encontrarlo
                Temp_Aguas=0
                for pokemon in Equipo[:3]:
                    #Mirar si hasta el tercero hay repetidos
                    if pokemon.tipo == "Agua":
                        Temp_Aguas +=1
                if Temp_Aguas <=1:
                    print("Tipo agua repetido ere el cuarto, cambiar posicion 4")
                    #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI AGUA NI DE LOS Q YA HAY
                    tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                    tipo_seleccionado = random.choice(tipos_con_valor_cero)
                    tipos[tipo_seleccionado] +=1
                    nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                    Equipo[3] = nuevo_pokemon
                elif Temp_Aguas >=2:
                    #Si el cuarto no era el repetido, se hace hasta encontrarlo
                    Temp_Aguas=0
                    for pokemon in Equipo[:2]:
                        #Mirar si hasta el segundo hay repetidos
                        if pokemon.tipo == "Agua":
                            Temp_Aguas +=1
                    if Temp_Aguas <=1:
                        print("Tipo agua repetido ere el tercero, cambiar posicion 3")
                        #AQUI PONER CODIGO PARA QUE ELIJA UNO QUE NO SEA NI AGUA NI DE LOS Q YA HAY
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[2] = nuevo_pokemon
                    elif Temp_Aguas >=2:
                        #Si el tercero no era el repetido, El primero y segundo son, asi que se cambia el segundo
                        print("Tipo agua repetido es el segundo")
                        tipos_con_valor_cero = [tipo for tipo, valor in tipos.items() if valor == 0]
                        tipo_seleccionado = random.choice(tipos_con_valor_cero)
                        tipos[tipo_seleccionado] +=1
                        nuevo_pokemon = obtener_pokemon_aleatorio(tipo_seleccionado)
                        Equipo[1] = nuevo_pokemon


print("El equipo sin Pokemons repetidos es:", end=' ')
for i in Equipo:
    print(i, end=' ')
