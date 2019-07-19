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
        #print(funciones_list_dic)
        ecuaciones=[]
        for i in range(len(funciones_list_dic)):
            #retorna una restricción y lo almacenamos como parte de la lista de ecuaciones
            self.problema+=self.crear_una_restriccion(funciones_list_dic[i]),"restriccion {}".format(i)
        
    
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
            coeficientes_f_objetivo.append(float(coeficientes[i])*self.variables[int(variables_pos[i])-1])
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
    
    def crear_una_restriccion(self,diccionario):
        auxiliar_ecuacion=[]
        for i in range(len(diccionario["coeficientes"])):
            auxiliar_ecuacion.append(float(diccionario["coeficientes"][i])*self.variables[int(diccionario["variables"][i])-1])
        
        objetivo=auxiliar_ecuacion[0]
        operadores_restriccion=[]
        #obtenemos los operadpres
        for i in range(len(diccionario["operadores"])-1):
            operadores_restriccion.append(diccionario["operadores"][i])
        #obtenemos el simbolo de la inecuacion
        comparador_final=diccionario["operadores"][len(diccionario["operadores"])-1]
        #obtenemos el valor a compararse de la inecuacion
        valor_comparado=diccionario["valor"][len(diccionario["valor"])-1]
        #print(operadores_restriccion,valor_comparado)
        for i in range(len(operadores_restriccion)):
            if operadores_restriccion[i]=="+":
                objetivo=objetivo+auxiliar_ecuacion[i+1]
            elif operadores_restriccion[i]=="-":
                objetivo=objetivo-auxiliar_ecuacion[i+1]
        
        if comparador_final=="<":
            objetivo=objetivo<=float(valor_comparado)
        elif comparador_final==">":
            objetivo=objetivo>=float(valor_comparado)
        elif comparador_final=="=":
            objetivo=objetivo==float(valor_comparado)
        print(objetivo)

        return objetivo
        #print(objetivo) // debe imprimir una restricción completa,por ejemplo: 3*x1+4*x2<=5
    
    def resolver_problema(self):
        self.problema.writeLP("pl.lp")
        self.problema.solve()
        print("Estado",LpStatus[self.problema.status])
        for v in self.problema.variables():
            print(v.name,"=",v.varValue)
        print("El resultado es: =",value(self.problema.objective))