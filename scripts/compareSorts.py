from lib.sortAlgorithms.quicksort import quicksort
from lib.sortAlgorithms.bubblesort import bubblesort
import time
from colorama import Fore

def compareSorts(puntosCombate):
    #Timsort Built-in Python
    print(Fore.MAGENTA+"Timsort Built-in Python"+Fore.RESET)
    time0 = time.time()
    sorted(puntosCombate.items(), key=lambda x: x[1]["puntosCombate"], reverse=True)
    print("El tiempo de ejecucion ha sido:",time.time()-time0)
    print("")

    #Quicksort Algorithm
    print(Fore.BLUE+"Quicksort: "+Fore.RESET)
    time0 = time.time()
    quicksort(list(puntosCombate.items()))[::-1]
    print(f"El tiempo de ejecucion ha sido:",time.time()-time0)
    print("")

    #Bubblesort Algorithm
    print(Fore.RED+"Bubblesort: "+Fore.RESET)
    time0 = time.time()
    bubblesort(list(puntosCombate.items()))[::-1]
    print(f"El tiempo de ejecucion ha sido:",time.time()-time0)
    print("")