def bubblesort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j][1]["puntosCombate"] > items[j+1][1]["puntosCombate"]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

# Uso de la función bubbleSort
# bubbleSort(sorted_pokemon)