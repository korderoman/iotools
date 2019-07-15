from tkinter import *
from tkinter import ttk
from views.programacion_lineal import *

if __name__ == "__main__":
    principal=Tk()
    principal.geometry("408x390")
    principal.resizable(False,False)
    pl=Programacion_Lineal(principal)
    principal.title(pl.titulo)
    principal.mainloop()    
