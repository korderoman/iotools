from pulp import *

class Resolucionador:
    def __init__(self,nombre_o,nombre_d,dic_o_cant,dic_d_cant,lista_listas_costos):
        self.nombres_o_lista=nombre_o
        self.nombres_d_lista=nombre_d
        self.diccionario_o_cantidades=dic_o_cant
        self.diccionario_d_cantidades=dic_d_cant
        self.lista_de_listas_costo_unitario=lista_listas_costos
        self.diccionario_costos_unitarios=None
    
    def resolver_problema(self):
        problema=pulp.LpProblem("Problema de Transporte",pulp.LpMinimize)
        #creamos el diccionario de costos
        self.diccionario_costos_unitarios=pulp.makeDict([self.nombres_o_lista,self.nombres_d_lista],self.lista_de_listas_costo_unitario,0)
        #creamos una lista de tuplas que contiene todas las rutas posibles de transporte
        rutas=[(c,b) for c in self.nombres_o_lista for b in self.nombres_d_lista]
        #creamos un diccionario que contiene la cantidad enviadad en las rutas
        cantidad_enviada_x_ruta=pulp.LpVariable.dicts("ruta",(self.nombres_o_lista,self.nombres_d_lista),lowBound=0,cat=pulp.LpInteger)
        #creamos la función objetivo
        problema+=sum([cantidad_enviada_x_ruta[c][b]*self.diccionario_costos_unitarios[c][b] for (c,b) in rutas]), "Función Objetivo"
        #agregamos la cantidad máxima posible de atender por distribuidor
        for c in self.nombres_o_lista:
            problema+=sum([cantidad_enviada_x_ruta[c][b] for b in self.nombres_d_lista])<=self.diccionario_o_cantidades[c],"Ofertas máximas por distribuidor %s"%c
        #agregamos la cantidad máxima que se demanda por cliente
        for b in self.nombres_d_lista:
            problema+=sum([cantidad_enviada_x_ruta[c][b] for c in self.nombres_o_lista])>=self.diccionario_d_cantidades[b],"Demandas máximas por clientes%s"%b
        #exportamos a un archivo LP
        problema.writeLP("problema.lp")
        problema.solve()
        #almacenamos las respuestas
        respuestas=[]
        texto="Estado: {}".format(pulp.LpStatus[problema.status])+"\n"
        respuestas.append(texto)
        for v in problema.variables():
            texto="{0:}={1:}".format(v.name,v.varValue) +"\n"
            respuestas.append(texto)
        texto="Costo total de transporte={}".format(problema.objective.value())
        respuestas.append(texto)

        return respuestas