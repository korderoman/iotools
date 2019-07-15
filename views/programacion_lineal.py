from tkinter import *
from tkinter import ttk
from  tools.deco_programacion_lineal import *
class Programacion_Lineal:
    
    def __init__(self,principal):
        self.variable_x=StringVar() #referencia a la cantidad de variables del problema
        self.frame_principal=principal
        self.titulo="Resolución de Programación Lineal"
        self.constante_margen_x=5
        self.funcion_x=StringVar() #referencia a la función objetivo
        self.implementar_interfaz(self.frame_principal)


    def implementar_interfaz(self,padre):
        #variables
        Label(padre,text="Indique las variables separados por comas:").grid(row=0,column=0,pady=2,padx=self.constante_margen_x,sticky=W)
        variables_cadena=Entry(padre,textvariable=self.variable_x,width=25)
        variables_cadena.grid(row=0,column=1,columnspan=2,pady=2,padx=self.constante_margen_x, sticky=W)
        #función objetivo
        Label(padre,text="Indique la función objetivo:").grid(row=1,column=0,pady=2,padx=self.constante_margen_x,sticky=W)
        funcion_objetivo_cadena=Entry(padre,textvariable=self.funcion_x,width=25)
        funcion_objetivo_cadena.grid(row=1,column=1,pady=2,padx=self.constante_margen_x,sticky=W)
        #maximizar o minimizar funcion
        Label(padre,text="Elija una opción:").grid(row=2,column=0,padx=self.constante_margen_x,pady=2,sticky=W)
        tipo_funcion_cadena=ttk.Combobox(padre,values=["Maximizar", "Minimizar"],state="readonly",width=22)
        tipo_funcion_cadena.current(0)
        tipo_funcion_cadena.grid(row=2,column=1,pady=2,padx=self.constante_margen_x,columnspan=2, sticky=W)
        #restricciones
        Label(padre,text="Indique las restricciones:").grid(row=3,column=0,pady=2,padx=self.constante_margen_x,sticky=W)
        restricciones_cadena=Text(padre,width=49,height=10)
        restricciones_cadena.grid(row=4,column=0,columnspan=3,pady=2,padx=self.constante_margen_x,sticky=W)    
        #respuesta
        Label(padre,text="Resultados:").grid(row=6,column=0,columnspan=3,pady=2,padx=self.constante_margen_x,sticky=W)
        respuestas_cadena=Text(padre,state=DISABLED,width=49,height=5)
        respuestas_cadena.grid(row=7,column=0,columnspan=3,sticky=W,pady=2,padx=self.constante_margen_x)
        #botón de ejecución
        ejecutar=Button(padre,text="Resolver",command=lambda:self.obtener_data(tipo_funcion_cadena.get(),restricciones_cadena.get(1.0,END),respuestas_cadena))
        ejecutar.grid(row=5,column=0,columnspan=3,pady=2,padx=self.constante_margen_x,sticky=W+E+N+S)
    
    def obtener_data(self,tipo_funcion,restricciones,respuestas):
        #tipo-funcion hace referencia a si es maximización o minimización
        #restricciones son recibidas como una cadena de texto
        #las respuestas son recibidas como el widget Text
        deco=Deco_PL(self.funcion_x.get(),restricciones,tipo_funcion,self.variable_x.get())
        deco.definir_variables()
        deco.funcion_objetivo()