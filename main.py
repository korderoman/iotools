from tkinter import *
from tkinter import ttk
from views.programacion_lineal import *
from views.ruta_critica import *

from views.index import *

if __name__ == "__main__":
    principal=Tk()
    principal.geometry("816x490")
    principal.resizable(False,False)
    
    index=Index(principal)
    #rc=Ruta_Crítica(principal)
    #pl=Programacion_Lineal(principal)
    #principal.title(pl.titulo)
    principal.title("Módulo de Investigación de Operaciones")
    principal.config(menu=index.mi_menu)
    principal.mainloop()    
