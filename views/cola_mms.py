from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst

class Cola_MMS:
    def __init__(self,ventana):
        self.mx=5
        self.my=2
        self.frame_principal=Frame(ventana)
        #variables
        self.tasa_de_llegada=DoubleVar()
        self.tasa_de_atencion=DoubleVar()
        self.costo_de_espera=DoubleVar()
        self.costos_de_atencion=DoubleVar()
        self.probabilidad=DoubleVar()
        self.cantidad_servidores=IntVar()
        #resultados
        self.resultados=None
        #se implementa la interfaz
        """ Aunque parezca redundante ya que el frame principal es accesible de forma global
        incluirlo como un parámetro ayuda a clarificar el rol que desempeña el frame"""
        self.implementar_interfaz(self.frame_principal) 

    def implementar_interfaz(self,padre):
        #numero de servidores
        Label(padre,text="Ingrese el número de servidores:").grid(row=0,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.cantidad_servidores).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #tasa de llegada
        Label(padre,text="Ingrese la tasa de llegada (\u03BB):").grid(row=1,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.tasa_de_llegada).grid(row=2,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        #tasa de atención
        Label(padre,text="Ingrese la tasa de atención (\u03BC):").grid(row=1,column=1,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.tasa_de_llegada).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #recomendación1 
        texto_recomendacion_costos=("Puede dejar este espacio tal como está, si el problema no indica la determinación de los costos.\n"
            "Si alguno de los problemas indica alguno de los costos y otro no, dejar en 0 aquellos valores que no estén indicados\n"
            "Recuerde que los costos están asociados a la unidad de tiempo descrita en el problema o tomada del \u03BB o \u03BC"
            )
        recomendacion_entrada1=tkst.ScrolledText(padre,wrap="word",height=4,bg="#F1F1F1")
        recomendacion_entrada1.grid(row=3,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        recomendacion_entrada1.insert(END,texto_recomendacion_costos)
        recomendacion_entrada1.config(state=DISABLED)
        #costos de atención
        Label(padre,text="Ingrese el costo de atención:").grid(row=4,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.costos_de_atencion).grid(row=5,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        #costos de espera
        Label(padre,text="Ingrese el costo de espera:").grid(row=4,column=1,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.costos_de_atencion).grid(row=5,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #recomendación2
        texto_recomendacion_probabilidades=("Si el problema lo requiere, puede indicar la probabilidad que existan x elementos en cola"
        " el módulo por defecto le brinda la información de que no existan elementos en cola es decir P(0)"
        )
        recomendacion_entrada2=tkst.ScrolledText(padre,wrap="word",height=3,bg="#F1F1F1")
        recomendacion_entrada2.grid(row=6,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        recomendacion_entrada2.insert(END,texto_recomendacion_probabilidades)
        recomendacion_entrada2.config(state=DISABLED)
        #probabilidad
        Label(padre,text="Ingrese la cantidad de elementos:").grid(row=7,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.probabilidad).grid(row=7,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #boton de ejecución
        Button(padre,text="Resolver",command=self.resolver).grid(row=8,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        #Resultados
        self.resultados=tkst.ScrolledText(padre,wrap="word",height=5,state=DISABLED)
        self.resultados.grid(row=9,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
    def resolver(self):
            pass
        