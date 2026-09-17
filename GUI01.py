import tkinter as tk
import matplotlib.pyplot as plp

x = [3,10, 21, 54]
y = [10, 14, 20 , 100]

plp.plot(x,y)
plp.scatter(x,y)# esta grafica es de puntos
plp.bar(x, y)#grafica de barras
plp.title("Mi primera Grafica")
plp.xlabel("eje x")
plp.ylabel("eje y")
plp.show()

def saludar():
    nombre = entrda.get().strip()
    if not nombre:
        nombre = "Carlos"
    lbl.config(text=f"Hola compa, {nombre}")


root = tk.Tk() #crear ventana
root.title("Minecraft Launcher") #el titulo
root.geometry("400x600") #el tamaño de ventana

lbl = tk.Label(root, text="Eh compa, Escribe tu nombre y presiona el boton", foreground="pink", background="purple")
lbl.pack(pady=10) #es la altura que va a tener el texto
entrda = tk.Entry(root)
entrda.pack(pady=10) 
bot = tk.Button(root, text="Saludar", foreground="red", background="blue", command=saludar)
bot.pack(pady=10)


root.mainloop()#esto es para que la ventana no se cierre y quede en un bucle