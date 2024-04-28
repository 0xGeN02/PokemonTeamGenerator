# Este algoritmo va a recibir un json del la forma 'Total Weaknesses': {'water': 1, 'ground': 3} y lo va a ordenar de mayor a menor segun el valor asociado
def quickSort(jsonData):
    if len(jsonData) <= 1:
        return jsonData
    else:
        pivot_key, pivot_value = jsonData.popitem()
        greater = {}
        lower = {}
        for key in jsonData:
            if jsonData[key] > pivot_value:
                greater[key] = jsonData[key]
            else:
                lower[key] = jsonData[key]
        return {**quickSort(greater), pivot_key: pivot_value, **quickSort(lower)}