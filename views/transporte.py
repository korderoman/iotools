from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tools.deco_transporte import *

class Transportes:
    def __init__(self,ventana):
        self.ventana=ventana
        self.frame_principal=Frame(self.ventana)
        #constante de separación
        self.constante_margen_x=5
        self.constante_margen_y=2
        self.ancho=25
        #variables de captura
        self.distribuidoras_nombres_variable=StringVar() #nombre de empresas que distribuyen el producto
        self.clientes_nombres_variables=StringVar() #nombre de empresas que demandan productos
        self.distribuidoras_cantidades_variable=StringVar() #cantidades máximas que pueden distribuir las empresas distribuidoras
        self.clientes_cantidades_variables=StringVar() #cantidades solicitadas por las empresas clientes
        self.costo_unitario_envio_distribuidora_cliente_variable=StringVar() #costo unitario de envío de distribuidora a empresa
        #variable de respuestas
        self.respuestas=None
        #se implementa la interfaz
        self.implementar_interfaz(self.frame_principal)

    def implementar_interfaz(self,padre):
        #distribuidoras nombres
        Label(padre,text="Ingrese el nombre de las entidades que ofertan\nseparados por comas:",justify=LEFT).grid(row=0,column=0, padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W)
        distribuidores_nombres_cadena=Entry(padre,textvariable=self.distribuidoras_nombres_variable)
        distribuidores_nombres_cadena.grid(row=1,column=0,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
        #distribuidoras cantidades
        Label(padre,text="Ingrese las cantidades de las entidades que ofertan\nseparados por comas:",justify=LEFT).grid(row=0,column=1,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W)
        distribuidores_cantidades_cadena=Entry(padre,textvariable=self.distribuidoras_cantidades_variable)
        distribuidores_cantidades_cadena.grid(row=1,column=1,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
        #clientes nombres
        Label(padre,text="Ingrese el nombre de las entidades que demandan\nseparados por comas:",justify=LEFT).grid(row=2,column=0,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W)
        clientes_nombres_cadena=Entry(padre,textvariable=self.clientes_nombres_variables)
        clientes_nombres_cadena.grid(row=3,column=0,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
        #clientes cantidades
        Label(padre,text="Ingrese las cantidades de las entidades que demandan\nseparados por comas:",justify=LEFT).grid(row=2,column=1,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W)
        clientes_cantidades_cadena=Entry(padre,textvariable=self.clientes_cantidades_variables)
        clientes_cantidades_cadena.grid(row=3,column=1,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
        #costos unitarios
        Label(padre,text="Ingrese los costos unitarios de cada entidades ofertante hacia\nlas entidades demandantes",justify=LEFT).grid(row=4,column=0,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W)
        costo_unitario_envio_distribuidora_cliente_cadena=Entry(padre,textvariable=self.costo_unitario_envio_distribuidora_cliente_variable)
        costo_unitario_envio_distribuidora_cliente_cadena.grid(row=5,column=0,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
        #texto que acompaña a los costos unitarios y su formato
        recomendacion_costos_unitarios=("Sea A,B ofertantes y X,Y demandan-tes, y los costos unitarios de  envío "
            "de A hacia X es ax1 y de A hacia Y ay1 y de B hacia X bx1 e Y by1 respectivamente tal que los costos se colocan "
            "ax1,ay1;bx1,by1 siendo el punto y coma la separación entre entidades ofertantes y la coma la separa-ción entre enti-dades demandantes")
        recomendacion_texto1=tkst.ScrolledText(padre,height=5, width=10,bg="#F1F1F1")
        recomendacion_texto1.grid(row=4, column=1, rowspan=2,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=NSEW)
        recomendacion_texto1.insert(END,recomendacion_costos_unitarios)
        recomendacion_texto1.config(state=DISABLED)
        #Botón de Ejecución
        Button(padre,text="Procesar", command=self.procesamiento).grid(row=6,column=0,columnspan=2, padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
        #configuramos la respuesta
        Label(padre,text="Respuestas:").grid(row=7,column=0,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W)
        self.respuestas=tkst.ScrolledText(padre,state=DISABLED,height=5, bg="#F1F1F1")
        self.respuestas.grid(row=8,column=0,columnspan=2,padx=self.constante_margen_x,pady=self.constante_margen_y,sticky=W+E)
    
    def procesamiento(self):
        deco=Deco_Transportes(self.distribuidoras_nombres_variable.get(),self.distribuidoras_cantidades_variable.get(),self.clientes_nombres_variables.get(),self.clientes_cantidades_variables.get(),self.costo_unitario_envio_distribuidora_cliente_variable.get())
        respuestas_retornadas=deco.procesar()
        self.respuestas.config(state="normal")
        self.respuestas.delete(1.0,END)
        for i in respuestas_retornadas:
            self.respuestas.insert(INSERT,i)  
        self.respuestas.config(state=DISABLED)