def calculate_competitiveValue(pokemon):
    competitiveValue = 0
    pokemonStats = 0
    moveStats = 0
    typeAdvantage = 0

    # Calculate weight based on stats
    pokemonStats += pokemon["stats"]["hp"]
    pokemonStats += pokemon["stats"]["attack"]
    pokemonStats += pokemon["stats"]["defense"]
    pokemonStats += pokemon["stats"]["spAttack"]
    pokemonStats += pokemon["stats"]["spDefense"]
    pokemonStats += pokemon["stats"]["speed"]
    pokemonStats /= 6
    
    # Calculate weight based on moves
    for _, value in pokemon["moves"].items():
        if value == "status":
            moveStats += 80
        else:
            moveStats += value

    moveStats /= 4
    
    # Calculate weight based on weaknesses and strengths
    typeAdvantage += len(pokemon["strengths"]) - len(pokemon["weaknesses"])
    
    competitiveValue = round(-100+ pokemonStats + moveStats + typeAdvantage*10,2)
    return competitiveValue