'''En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, 
también debe de tener un label con el texto que queráis.'''

import tkinter
from tkinter import ttk

window = tkinter.Tk()

label = ttk.Label(window, text='Seleccionar color')
label.pack(anchor='nw')

listaColores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Violeta']
listaColores_items = tkinter.StringVar(value=listaColores)
listbox = tkinter.Listbox(window, height=25, listvariable=listaColores_items)
listbox.pack(anchor='nw')



window.mainloop()
