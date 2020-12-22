from tkinter import*

window = Tk()

window.title("APITKINTER")

lbl = Label(window,text="Bienvenido!", )#font=("Arial Bold",50)

lbl.grid(column=0, row=0)



txt= Entry(window,width=10)#desabilitar TXT de entrada *stated='disabled'*
txt.grid(column=1,row=0)
window.geometry('350x200')#tamaño de la ventana

def clicked():

    res= "Hola "+txt.get()#PRalabra predeterminada + txt escrito
    lbl.configure(text= res)#muestra palabra predeterminada +TXT escrito
txt.focus()#focus de entrada para escribir

btn=Button(window,text=("Click Me"),bg=("black"),fg=("white"),command=clicked)#crea un boton
btn.grid(column=2, row=0)



window.mainloop()