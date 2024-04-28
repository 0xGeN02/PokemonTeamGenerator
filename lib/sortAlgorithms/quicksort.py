def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2][1]["puntosCombate"]
    left = [x for x in items if x[1]["puntosCombate"] < pivot]
    middle = [x for x in items if x[1]["puntosCombate"] == pivot]
    right = [x for x in items if x[1]["puntosCombate"] > pivot]
    return quicksort(left) + middle + quicksort(right)
# Uso de la función quicksort
# sorted_pokemon = quicksort(list(puntosCombate.items()))[::-1]