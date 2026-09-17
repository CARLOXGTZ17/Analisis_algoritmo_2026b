#____________________________SORTS____________________________
#BubbleSort
def bubble_sort_brute_fort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#numeros = [24,15,36,24,65,78]
#print("lista ordenada", bubble_sort_brute_fort(numeros))

#SelectionSort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = 1
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#numeros = [24,15,36,24,65,78]
#print("lista ordenada", selection_sort(numeros))

#GnomeSort
def gnome_sort(lista):
    arr = lista.copy()
    i = 0
    n = len(arr)
    
    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1  # Avanza si está en orden
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Intercambia
            i -= 1  # Retrocede un paso
            
    return arr

#StoogeSort
#def stooge_sort_rec(arr, l, h):
    if l >= h:
        return

    # Si el primer elemento es mayor que el último, intercambiar
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    # Si hay 3 o más elementos en el rango
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        # Aplicar fuerza bruta a los 3 tercios superpuestos
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3
        stooge_sort_rec(arr, l + t, h)       # Últimos 2/3
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3 de nuevo

#def stooge_sort(lista):
    arr = lista.copy()
    stooge_sort_rec(arr, 0, len(arr) - 1)
    return arr

#ExchangeSort
def exchange_sort(lista):
    """
    Ordenamiento por Intercambio Directo (Exchange Sort).
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Si el elemento posterior es menor, intercambia de inmediato
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

#InsertSort
def insertion_sort(lista):
    """
    Ordenamiento por Inserción.
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        # Compara la clave con los elementos anteriores y los desplaza
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

#Quick Sort
def quick_sort(arr):
    # Caso base: una lista vacía o con un solo elemento ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Elección del pivote (en este caso, el elemento central)
    pivot = arr[len(arr) // 2]
    
    # Particionamiento de la lista
    izq = [x for x in arr if x < pivot]
    centro = [x for x in arr if x == pivot]
    der = [x for x in arr if x > pivot]
    
    # Llamada recursiva combinando los resultados
    return quick_sort(izq) + centro + quick_sort(der)

numeros = [24,15,36,24,65,78]
print("lista ordenada con quick", quick_sort(numeros))


#Marge Sort
def merge_sort(arr):
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(arr) <= 1:
        return

    # 1. DIVIDE: Encontrar el punto medio y dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. VENCE: Llamadas recursivas para ordenar cada mitad
    merge_sort(left_half)
    merge_sort(right_half)

    # 3. COMBINA (Merge): Fusionar las dos mitades ordenadas en la lista original
    i = j = k = 0

    # Comparar elementos de ambas mitades y colocar el menor en 'arr'
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Verificar si quedaron elementos en la mitad izquierda
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    # Verificar si quedaron elementos en la mitad derecha
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
numeros = [24,15,36,24,65,78]
print("lista desordenada", numeros)
merge_sort(numeros)
print("lista ordenada con merge", numeros)


#_____________________________________________________________