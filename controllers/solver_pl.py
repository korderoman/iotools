from pulp import *

class Resolucionador:
    def __init__(self,tipo_problema):
        self.tipo=LpMinimize
        if tipo_problema=="Maximizar":
            self.tipo=LpMaximize

        self.problema=LpProblem("Resolución",self.tipo)
        self.variables=[] #lista de variables de pulp
            
    def crear_funciones_restricciones(self,funciones_list_dic):
        #la función recibe una lista de diccionarios donde cada diccionario representa una ecuación
        pass

    def crear_funcion_objetivo(self, coeficientes,variables_pos,operadores):
        #creamos cada uno de los coeficientes
        coeficientes_f_objetivo=[]
        for i in range(len(coeficientes)):
            """
            obtenemos los componentes de la función objetivo, es decir, un componente por ejemplo puede ser 4x1, 4 es parte de los
            elementos de la lista de coeficientes x1 es de la lista de variables que ya se formo en la función crear variables,
            entonces 4x1 se obtiene de multiplicar la posicion 0 de la lista de coeficientes con la posición que se obtiene del valor de
            la variable_posicion disminuyendo en uno-> int(variables_pos[i]-1) y que buscamos en la lista de variables 
            """
            coeficientes_f_objetivo.append(int(coeficientes[i])*self.variables[int(variables_pos[i])-1])
        #la función objetivo toma al primer valor de la lista de coeficientes_f_objetivo y dado que la lista de operadores tiene una longitud
        #menor en 1 a la longitud de coeficientes_f_objetivo se realiza el sigte código
        #donde se evalúa si el operador es suma o resta, no existe otra opción, no al menos en PL
        objetivo=coeficientes_f_objetivo[0]
        for i in range(len(operadores)):
            if operadores[i]=="+":
                objetivo=objetivo+coeficientes_f_objetivo[i+1]
            else: #este valor evita que se crashee el programa; sin embargo, hace que siempre sea un menos y la respuesta puede ser equivocada
                objetivo=objetivo-coeficientes_f_objetivo[i+1]
        
        #print(coeficientes_f_objetivo,objetivo) //el objetivo es la función objetivo en toda su dimensión, ahora debemos de colocarlo en pulp
        self.problema+=objetivo,"función objetivo"
        print("Todo está ok")
    def crear_variables(self,variables_lista):
        self.variables=[LpVariable(i,0,None) for i in variables_lista]#creamos las variables que tendrán como nombre el valor de cada elemento de la lista, es decir x1,x2 .... xn
        #print(type(self.variables[0])) //pulp.pulp.LpVariable