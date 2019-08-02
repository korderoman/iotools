from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tools.deco_ruta_critica import *
class Ruta_Crítica:
    def __init__(self,principal):
        self.const_margen_x=5
        self.const_margen_y=2
        self.titulo="Resolución de Ruta Crítica"
        self.nodos_cadena_variable="" #una entrada de texto no recibe una variable como las Entry
        self.arcos_cadena_variable=StringVar()
        self.frame_izquierdo=Frame(principal)
        self.frame_izquierdo.pack(side="left",fill=Y)
        self.frame_derecho=Frame(principal)
        self.frame_derecho.pack(side="left",fill=Y)
        self.respuestas=None
        self.implementar_interfaz(self.frame_izquierdo)


    def implementar_interfaz(self,padre):
        
        Label(padre,text="Ingrese como (a,b) los nodos \n y separados por comas: ").grid(row=0,column=0,columnspan=2,pady=self.const_margen_y,padx=self.const_margen_x,sticky=W )
        nodos_cadena=tkst.ScrolledText(padre,wrap="word",width=20,height=8)
        nodos_cadena.grid(row=1,column=0,pady=self.const_margen_y,padx=self.const_margen_x,sticky=W)

        Label(padre,text="Ingrese el valor de los arcos \n por pareja de nodos  \n separados por comas: ").grid(row=2,column=0,padx=self.const_margen_x,pady=self.const_margen_y,sticky=W)
        arcos_cadena=Entry(padre,textvariable=self.arcos_cadena_variable,width=30)
        arcos_cadena.grid(row=3,column=0,padx=self.const_margen_x,pady=self.const_margen_y,sticky=W) 
        Label(padre,text="Ruta Crítica: ").grid(row=4,column=0,padx=self.const_margen_x,pady=self.const_margen_y,sticky=W)
        self.respuestas=Text(padre,width=20,height=5,state=DISABLED)
        self.respuestas.grid(row=5,column=0,pady=self.const_margen_y,padx=self.const_margen_x,sticky=W+E+N+S)
        #el botón es la última implementación
        boton_ejecutar=Button(padre,text="Obtener Ruta Crítica",command=lambda:self.obtener_data(nodos_cadena.get(1.0,END),self.arcos_cadena_variable.get()) )
        boton_ejecutar.grid(row=4,column=0,pady=self.const_margen_y,padx=self.const_margen_x,sticky=W+E+N+S)
   
    def obtener_data(self,nodos_cadena_parametro,arcos_cadena_parametro):
        #print(nodos_cadena_parametro,arcos_cadena_parametro)
        deco=Deco_RC(nodos_cadena_parametro,arcos_cadena_parametro,self.frame_derecho)
        ruta,longitud=deco.resolucion()
        #print(ruta,longitud)
        
        self.respuestas.config(state="normal")
        self.respuestas.delete(1.0,END)
        self.respuestas.insert(INSERT,"La ruta crítica es: "+str(ruta)+"\n")
        self.respuestas.insert(INSERT,"El tiempo total es: "+str(longitud))
        self.respuestas.config(state=DISABLED)
        