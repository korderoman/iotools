from tkinter import *
from tkinter import ttk
from views.programacion_lineal import *
from views.ruta_critica import *
from tkinter import messagebox
from views.index import *

if __name__ == "__main__":
    principal=Tk()
    ancho_programa=816
    alto_programa=490
    ancho_pantalla=principal.winfo_screenwidth()
    alto_pantalla=principal.winfo_screenheight()

    posicion_x=(ancho_pantalla/2)-(ancho_programa/2)
    posicion_y=(alto_pantalla/2)-(alto_programa/2)

    principal.geometry("%dx%d+%d+%d"%(ancho_programa,alto_programa,posicion_x,posicion_y))
    principal.resizable(False,False)
    
    index=Index(principal)
    principal.title("Módulo de Investigación de Operaciones")
    principal.config(menu=index.mi_menu)
    
    def salir():
        if messagebox.askokcancel("Salir de IO Tools","¿Está seguro que desea salir?"):
            principal.quit()
            principal.destroy()  
    principal.protocol("WM_DELETE_WINDOW",salir)
    principal.mainloop()


