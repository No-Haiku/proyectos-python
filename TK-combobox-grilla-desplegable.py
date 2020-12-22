from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Bienvendo a las practicas")

window.geometry('350x200')

combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5, "Text")

combo.current(0) #set deseleccion empieza en el 0 muestra el 1
combo.grid(column=4, row=0)




window.mainloop()
