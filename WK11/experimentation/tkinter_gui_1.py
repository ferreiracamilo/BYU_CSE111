import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")
ventana.title("My App")

def saludo(nombre):
    print(f"Hola {nombre}")

lbl = tkinter.Label(ventana, text = "Este es un [Label] tkinter")
lbl.pack()

btn = tkinter.Button(ventana, text="Presiona este button para mensaje", command = saludo("rodolfo"))

boton1 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5)
boton2 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5)
boton3 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5)
boton4 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5)

# boton1.grid(row = 0, column = 0)
#boton2.grid(row = 1, column = 0)
#boton3.grid(row = 2, column = 1)
#boton4.grid(row = 3, column = 1)

#boton1 = tkinter.Button(ventana, text = "Presiona", command = lambda: saludo("python"))
#boton1.pack

ventana.mainloop()