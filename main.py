from tkinter import *
from tkinter import ttk
from views.programacion_lineal import *
from views.ruta_critica import *

if __name__ == "__main__":
    principal=Tk()
    principal.geometry("816x490")
    principal.resizable(False,False)
    rc=Ruta_Crítica(principal)
    #pl=Programacion_Lineal(principal)
    #principal.title(pl.titulo)
    principal.title(rc.titulo)
    principal.mainloop()    
