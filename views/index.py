from tkinter import *
from tkinter import ttk
#importamos las vistas de los modulos
from views.programacion_lineal import *
from views.ruta_critica import *
from views.ruta_critica import *
from views.transporte import *
from views.cola_mms import *
class Index():
    def __init__(self,ventana):
        self.ventana=ventana
        self.mi_menu=None
        self.crear_menu()
       

        #frames de la bienvenida
        self.frame_de_inicio=Frame(self.ventana)
        self.frame_inicio()  
        self.frame_de_inicio.pack(fill=BOTH)
        #instancia del modulo de programacion lineal continua
        self.frame_de_pl_continua=Programacion_Lineal(self.ventana)
        #instancia del modulo de la ruta crítica
        self.frame_de_ruta_critica=Ruta_Crítica(self.ventana) 
        #instancia del módulo de transportes
        self.frame_de_transportes=Transportes(self.ventana)
        #instancia del módulo de colas MMS
        self.frame_de_colasMMS=Cola_MMS(self.ventana)
         #almacenamos todos los frames
        self.frames=[
                    self.frame_de_inicio,
                    self.frame_de_pl_continua.frame_principal,
                    self.frame_de_ruta_critica.frame_principal,
                    self.frame_de_transportes.frame_principal,
                    self.frame_de_colasMMS.frame_principal
                    ]        
        
        self.nombres=["Inicio","PL Contínua","Ruta Crítica","PL Transporte","M/M/S"]


    def frame_inicio(self):
        texto="Bienvenido a IO Tools, los elementos que encontrarás en el menú te permitirán \n idea clara del procesamiento de los tópicos de investigación de operaciones tanto en 1 y 2 \n Hecho por Kordero"
            
        Label(self.frame_de_inicio,text=texto).grid(column=0,row=0) 


    def llamada_io_tool(self,submenu,pos):
        menu_elegido=submenu.entrycget(pos,"label")
        print(menu_elegido)

        for index,menu in enumerate(self.nombres):
            if(menu==menu_elegido):
                self.frames[index].pack(fill=BOTH)
            else:
                self.frames[index].pack_forget()

    

    def crear_menu(self):
        #un menu se pega a la ventana 
        self.mi_menu=Menu(self.ventana)
        #agregamos los submenus para el menu
        programacion_lineal_sub_menu=Menu(self.mi_menu,tearoff=0)
        redes_sub_menu=Menu(self.mi_menu,tearoff=0)
        programacion_dinamica_sub_menu=Menu(self.mi_menu,tearoff=0)
        colas_sub_menu=Menu(self.mi_menu,tearoff=0)

        #creamos los elementos de los submenus
        programacion_lineal_sub_menu.add_command(label="PL Contínua",underline=0, command=lambda:self.llamada_io_tool(programacion_lineal_sub_menu,0))
        programacion_lineal_sub_menu.add_command(label="PL Entera",underline=0, command=lambda:self.llamada_io_tool(programacion_lineal_sub_menu,1))
        programacion_lineal_sub_menu.add_command(label="PL Transporte",underline=0, command=lambda:self.llamada_io_tool(programacion_lineal_sub_menu,2))
        programacion_lineal_sub_menu.add_command(label="PL Sensibilidad",underline=0, command=lambda:self.llamada_io_tool(programacion_lineal_sub_menu,3))

        redes_sub_menu.add_command(label="Ruta Crítica",underline=0, command=lambda:self.llamada_io_tool(redes_sub_menu,0))
        redes_sub_menu.add_command(label="Flujo Máximo",underline=0, command=lambda:self.llamada_io_tool(redes_sub_menu,1))
        redes_sub_menu.add_command(label="Camino Mínimo",underline=0, command=lambda:self.llamada_io_tool(redes_sub_menu,2))
        
        programacion_dinamica_sub_menu.add_command(label="PD Determinística", underline=0, command=lambda:self.llamada_io_tool(programacion_dinamica_sub_menu,0))
        programacion_dinamica_sub_menu.add_command(label="PD Probabilística", underline=0, command=lambda:self.llamada_io_tool(programacion_dinamica_sub_menu,1))
        
        colas_sub_menu.add_command(label="M/M/1", underline=0,command=lambda:self.llamada_io_tool(colas_sub_menu,0))
        colas_sub_menu.add_command(label="M/M/S", underline=0,command=lambda:self.llamada_io_tool(colas_sub_menu,1))
        
        self.mi_menu.add_command(label="Inicio", command=lambda:self.llamada_io_tool(self.mi_menu,1))
        self.mi_menu.add_cascade(label="Programación Lineal",menu=programacion_lineal_sub_menu)
        self.mi_menu.add_cascade(label="Redes",menu=redes_sub_menu)
        self.mi_menu.add_cascade(label="Programación Dinámica",menu=programacion_dinamica_sub_menu)
        self.mi_menu.add_cascade(label="Colas",menu=colas_sub_menu)

    

        
