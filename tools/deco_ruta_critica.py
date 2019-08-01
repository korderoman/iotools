from ast import literal_eval as evaluador_string
from  controllers.solver_rc import *

class Deco_RC:
    def __init__(self,nodos_cadenas_parametro,arcos_cadenas_parametro):
        self.nodos_cadenas=nodos_cadenas_parametro
        self.arcos_cadenas=arcos_cadenas_parametro
        self.problema=Resolucionador(self.decodificar_nodos(self.nodos_cadenas),self.decodificar_arcos(self.arcos_cadenas))
        #self.decodificar_nodos(self.nodos_cadenas)

    
    def decodificar_nodos(self,nodos_cadenas):
        #obtenemos una lista que tiene como elemento a cada tupla  "(1,2)" pero como String
        lista_tuplas_cadenas=nodos_cadenas.split(";")
        #evaluamos cada elemento y parseamos a tupla
        lista_tuplas=[evaluador_string(x) for x in lista_tuplas_cadenas]
        return lista_tuplas

    def decodificar_arcos(self,arcos_cadenas):
        #obtenemos la lista de arcos donde cada elementos es una cadena
        lista_arcos_cadenas=arcos_cadenas.split(",")
        #parseamos a decimales los elementos de la lista anterior
        lista_arcos=[float(x) for x in lista_arcos_cadenas]
        return lista_arcos

    def resolucion(self):
        ruta,longitud=self.problema.resolucion()
        return ruta,longitud
    