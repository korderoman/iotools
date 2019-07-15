from pulp import *

class Resolucionador:
    def __init__(self,tipo_problema):
        self.tipo=LpMinimize
        if tipo_problema=="Maximizar":
            self.tipo=LpMaximize

        self.problema=LpProblem("Resolución",self.tipo)
        self.variables=[] #lista de variables de pulp
            
    def crear_funciones_limitantes(self,coeficientes,variables,operadores,valores):
        pass

    def crear_funcion_objetivo(self, coeficientes,variables_pos,operadores):
        #creamos cada uno de los coeficientes
        coeficientes_f_objetivo=[]
        for i in range(len(coeficientes)):
            coeficientes_f_objetivo.append(int(coeficientes[i])*self.variables[int(variables_pos[i])])
        print(coeficientes_f_objetivo)
    def crear_variables(self,variables_lista):
        self.variables=[LpVariable(i,0,None) for i in variables_lista]#creamos las variables que tendrán como nombre el valor de cada elemento de la lista, es decir x1,x2 .... xn
        #print(type(self.variables[0])) //pulp.pulp.LpVariable