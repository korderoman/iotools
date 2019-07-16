import re
from controllers.solver_pl import *
class Deco_PL:
    def __init__(self,funcion_objetivo,restricciones, tipo_funcion,cant_variables ):
        self.funcion_objetivo_cadena=funcion_objetivo #referencia a la función objetivo recibida como una cadena
        self.restricciones_cadena=restricciones #referencia a las ecuaciones de las restricciones recibidas como una cadena
        self.tipo_funcion_cadena=tipo_funcion #referencia al tipo de optimización, es decir maximización o minimización, es recibida como una cadena
        self.cantidad_variables_cadena=cant_variables #referencia a la cantidad de variables del problema
        self.resolver=Resolucionador(self.tipo_funcion_cadena)
    def funcion_objetivo(self):
        componentes=re.split(r"[+,\-]",self.funcion_objetivo_cadena)
        operadores=[x for x in self.funcion_objetivo_cadena if x=="+" or x=="-"]

        intermedio=[]
        coeficientes=[]
        variables=[]

        for i in componentes:
            aux=i.split("x")
            intermedio.append(aux)
        coeficientes=[i[0] for i in intermedio] #obtenemos los coeficientes
        variables=[i[1] for i in intermedio]#obtenemos el valor de las variables
        self.resolver.crear_funcion_objetivo(coeficientes,variables,operadores)
        #print(componentes,operadores,coeficientes, variables) //verifica las listas que se están enviando
       
    def funciones_restricciones(self):
        self.restricciones_cadena=self.restricciones_cadena.split("\n")
        self.restricciones_cadena=[restriccion for restriccion in self.restricciones_cadena if restriccion]
        #print(self.restricciones_cadena) //puede revisar la salida de la lista de cadenas tal que cada cadena es una ecuación
        #obtenemos una lista de diccionarios, tal que cada diccionario representa una ecuación de restricción
        restricciones=[self.obtener_una_restriccion(ecuacion_cadena) for ecuacion_cadena in self.restricciones_cadena]
        #print(restricciones) //revisión si las restricciones se encuentran en formato de diccionario
        self.resolver.crear_funciones_restricciones(restricciones)
    def definir_variables(self):
        #recibimos como parámetros una cadena
        variables_cadena=self.cantidad_variables_cadena.split(",") #la cadena es convertida a una lista de cadenas donde cada elemento se obtiene cuando se encuentra una coma
        self.resolver.crear_variables(variables_cadena)

    def obtener_una_restriccion(self,funcion):
        
        componentes=re.split(r"[+,\-,=,<=,>=]",funcion)#obtenemos la lista con los nombres de variables incluidos los espacios en blanco
        componentes=[x for x in componentes if x] #depuramos la lista elminando las cadenas vacias, quedando modelos #X# y en cola un número
        #recordar que en PL no existe el mayor o menor sino siempre es mayor igual que y menor igual que
        operadores=[x for x in funcion if x=="=" or x=="+" or x=="-" or x=="<" or x==">"] #obtenemos los operadores y almacenamos en una lista
        #de los componentes obtenemos los coeficientes y el orden de las variables
        intermedio=[]
        coeficientes=[]
        variables=[]

        for i in componentes:
            auxiliar=i.split("x")
            intermedio.append(auxiliar)
        #obtenemos los coeficientes        
        for i in range(len(intermedio)-1):
            coeficientes.append(intermedio[i][0])
        #obtenemos la numeración de la variable
        for i in range(len(intermedio)-1):
            variables.append(intermedio[i][1])
        
        valor=intermedio[(len(intermedio)-1)]
        #almacenamos la ecuación en un diccionario
        ecuacion={"coeficientes":coeficientes,"variables":variables,"operadores":operadores,"valor":valor}
        #print(intermedio,coeficientes,variables,valor)
        #print(ecuacion)
        return ecuacion