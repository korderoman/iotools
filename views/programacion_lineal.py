from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
from  tools.deco_programacion_lineal import *
class Programacion_Lineal:
    
    def __init__(self,ventana):
        self.variable_x=StringVar() #referencia a la cantidad de variables del problema
        self.ventana=ventana
        self.frame_principal=Frame(ventana)
        self.titulo="Resolución de Programación Lineal"
        self.constante_margen_x=5
        self.funcion_x=StringVar() #referencia a la función objetivo
        self.ancho=25
        self.implementar_interfaz(self.frame_principal)
        
        


    def implementar_interfaz(self,padre):
        #variables
        Label(padre,text="Indique las variables separados por comas:").grid(row=0,column=0,pady=2,padx=self.constante_margen_x,sticky=W)
        variables_cadena=Entry(padre,textvariable=self.variable_x,width=self.ancho)
        variables_cadena.grid(row=0,column=1,columnspan=2,pady=2,padx=self.constante_margen_x, sticky=W)
        #función objetivo
        Label(padre,text="Indique la función objetivo:").grid(row=0,column=3,pady=2,padx=self.constante_margen_x,sticky=W)
        funcion_objetivo_cadena=Entry(padre,textvariable=self.funcion_x,width=self.ancho)
        funcion_objetivo_cadena.grid(row=0,column=4,pady=2,padx=self.constante_margen_x,sticky=W)
        #maximizar o minimizar funcion
        Label(padre,text="Elija una opción:").grid(row=2,column=0,padx=self.constante_margen_x,pady=2,sticky=W)
        tipo_funcion_cadena=ttk.Combobox(padre,values=["Maximizar", "Minimizar"],state="readonly",width=self.ancho-3)
        tipo_funcion_cadena.current(0)
        tipo_funcion_cadena.grid(row=2,column=1,pady=2,padx=self.constante_margen_x,columnspan=2, sticky=W)
        #restricciones
        Label(padre,text="Indique las restricciones:").grid(row=3,column=0,pady=2,padx=self.constante_margen_x,sticky=W)
        restricciones_cadena=tkst.ScrolledText(padre,width=self.ancho+24,height=10, wrap="word")
        restricciones_cadena.grid(row=4,column=0,columnspan=3,pady=2,padx=self.constante_margen_x,sticky=W)    
        #texto que acompaña a las restricciones
        recomendacion_restricciones=("Recordar las que restricciones son las  ecuaciones a  las  que "
        "está  sujeta  la función   objetivo,  una  restricción   debe ocupar una línea, por ejemplo:\n"
        "4x1+2x2<5\n3x1-3x2<1\nY así sucesivamente cuantas ecuaciones  considere"
        )

        recomendacion_texto1=Text(padre, height=10,width=self.ancho+15,bg="#F1F1F1")
        recomendacion_texto1.grid(row=4,column=3,columnspan=2,pady=2,padx=self.constante_margen_x,sticky=N+S)
        recomendacion_texto1.insert(END,recomendacion_restricciones)
        recomendacion_texto1.config(state=DISABLED)
        #respuesta
        Label(padre,text="Resultados:").grid(row=6,column=0,columnspan=3,pady=2,padx=self.constante_margen_x,sticky=W)
        respuestas_cadena=tkst.ScrolledText(padre,state=DISABLED,width=(self.ancho+22)*2,height=5)
        respuestas_cadena.grid(row=7,column=0,columnspan=6,sticky=W,pady=2,padx=self.constante_margen_x)
        #botón de ejecución
        ejecutar=Button(padre,text="Resolver",command=lambda:self.obtener_data(tipo_funcion_cadena.get(),restricciones_cadena.get(1.0,END),respuestas_cadena))
        ejecutar.grid(row=5,column=0,columnspan=6,pady=2,padx=self.constante_margen_x,sticky=W+E+N+S)
    
    def obtener_data(self,tipo_funcion,restricciones,respuestas):
        #tipo-funcion hace referencia a si es maximización o minimización
        #restricciones son recibidas como una cadena de texto
        #las respuestas son recibidas como el widget Text
        deco=Deco_PL(self.funcion_x.get(),restricciones,tipo_funcion,self.variable_x.get())
        deco.definir_variables()
        deco.funcion_objetivo()
        deco.funciones_restricciones()
        deco.resolver_problema()