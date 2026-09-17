#____________________________IMPORTS___________________________
import matplotlib.pyplot as plt
import random as rd
import time as tm
import ordenamientos as ord
#_____________________________________________________________
#____________________________RANDOM___________________________
listas=[]
N = []
tiempos_bubble = []
tiempos_select = []
tiempos_gnome = []
tiempos_exchange = []
tiempos_insert = []
#tiempos_stooge = []
tiempos_quick = []
tiempos_merge = []


def genera (n, min, max):
    return[rd.randint(min,max) for i in range(n)]
#_____________________________________________________________
#____________________________FUNCION DEL BOTON_________________
def generar_y_calcular(inicio, incremento, fin):
    global listas, N, tiempos_bubble, tiempos_select, tiempos_gnome, tiempos_exchange, tiempos_insert, tiempos_stooge, tiempos_quick, tiempos_merge

    N = [i for i in range(inicio, fin + 1, incremento)]

    listas = []
    for i in N:
        listas.append(genera(i,1,100))
    print(listas)

    tiempos_bubble = []
    tiempos_select = []
    tiempos_gnome = []
    tiempos_exchange = []
    tiempos_insert = []
    #tiempos_stooge = []
    tiempos_quick = []
    tiempos_merge = []

    for lista in listas:
        copia1 = lista.copy()
        t0 = tm.perf_counter()
        ord.bubble_sort_brute_fort(copia1)
        tiempos_bubble.append(tm.perf_counter() - t0)

        copia2 = lista.copy()
        t0 = tm.perf_counter()
        ord.selection_sort(copia2)
        tiempos_select.append(tm.perf_counter() - t0)

        copia3 = lista.copy()
        t0 = tm.perf_counter()
        ord.gnome_sort(copia3)
        tiempos_gnome.append(tm.perf_counter() - t0)

        copia4 = lista.copy()
        t0 = tm.perf_counter()
        ord.exchange_sort(copia4)
        tiempos_exchange.append(tm.perf_counter() - t0)

        copia5 = lista.copy()
        t0 = tm.perf_counter()
        ord.insertion_sort(copia5)
        tiempos_insert.append(tm.perf_counter() - t0)

        #copia6 = lista.copy()
        #t0 = tm.perf_counter()
        #ord.stooge_sort(copia6)
        #tiempos_stooge.append(tm.perf_counter() - t0)  

        copia7 = lista.copy()
        t0 = tm.perf_counter()
        ord.quick_sort(copia7)
        tiempos_quick.append(tm.perf_counter() - t0)

        copia8 = lista.copy()
        t0 = tm.perf_counter()
        ord.merge_sort(copia8)
        tiempos_merge.append(tm.perf_counter() - t0)
#_____________________________________________________________