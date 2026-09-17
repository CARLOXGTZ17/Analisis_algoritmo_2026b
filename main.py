#____________________________IMPORTS___________________________
import tkinter as tk
import matplotlib.pyplot as plt
import benchmark as bnm
#_____________________________________________________________
#_____________________________GUI_____________________________
root = tk.Tk()
root.title("Comparar Algoritmos De Ordenamiento")
root.geometry("400x400")

lbl = tk.Label(root, text="Compara Los Algoritmos De Ordenamiento")
lbl.pack(pady=10)

lbl_entrada1 = tk.Label(root, text="Inicio")
lbl_entrada1.pack(pady=10)

entrada = tk.Entry(root)
entrada.pack(pady=10)

lbl_entrada2 = tk.Label(root, text="Incremento")
lbl_entrada2.pack(pady=10)

entrada2 = tk.Entry(root)
entrada2.pack(pady=10)

lbl_entrada3 = tk.Label(root, text="Fin")
lbl_entrada3.pack(pady=10)

entrada3 = tk.Entry(root)
entrada3.pack(pady=10)

#_______________________FUNCION DEL BOTON______________________
def calcular_y_graficar():
    inicio = int(entrada.get())
    incremento = int(entrada2.get())
    fin = int(entrada3.get())

    bnm.generar_y_calcular(inicio, incremento, fin)

    #_______________________PRIMERA GRAFICA_______________________
    plt.plot(bnm.N, bnm.tiempos_bubble, label="Bubble Sort",marker= "o")
    plt.plot(bnm.N, bnm.tiempos_select, label="Selection Sort",marker= "o")
    plt.plot(bnm.N, bnm.tiempos_gnome, label="Gnome Sort",marker= "o")
    plt.plot(bnm.N, bnm.tiempos_exchange, label="Exchange Sort",marker= "o")
    plt.plot(bnm.N, bnm.tiempos_insert, label="Insert Sort",marker= "o")
    plt.plot(bnm.N, bnm.tiempos_merge, label="Merge Sort",marker= "o")
    plt.plot(bnm.N, bnm.tiempos_quick, label="Quick Sort",marker= "o")

    plt.scatter(bnm.N, bnm.tiempos_merge)
    plt.scatter(bnm.N, bnm.tiempos_quick)
    plt.scatter(bnm.N, bnm.tiempos_bubble)
    plt.scatter(bnm.N, bnm.tiempos_select)
    plt.scatter(bnm.N, bnm.tiempos_gnome)
    plt.scatter(bnm.N, bnm.tiempos_exchange)
    plt.scatter(bnm.N, bnm.tiempos_insert)
    plt.title("COMPARAR ALGORITMOS DE ORDENAMINENTO")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend()
    plt.show()
    #_____________________________________________________________
    #_______________________SEGUNDA GRAFICA_______________________
    #plt.plot(bnm.N, bnm.tiempos_merge, label="Merge Sort")
    #plt.plot(bnm.N, bnm.tiempos_quick, label="Quick Sort")

    #plt.scatter(bnm.N, bnm.tiempos_merge, marker= "o")
    #plt.scatter(bnm.N, bnm.tiempos_quick, marker= "o")
    #plt.title("Grafica del Merge y Quick")
    #plt.xlabel("Eje x")
    #plt.ylabel("Eje y")
    #plt.legend()
    #plt.show()
    #_____________________________________________________________

btn_calcular = tk.Button(root, text="Calcular y Graficar", command=calcular_y_graficar)
btn_calcular.pack(pady=10)
#_____________________________________________________________

root.mainloop()