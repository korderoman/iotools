from controllers.solver_tr import *

class Deco_Transportes:
    def __init__(self,nombres_ofertantes,cantidades_ofertantes,nombres_demandantes,cantidades_demandantes,costos_unitarios):
        self.nombres_o_cadena=nombres_ofertantes
        self.nombres_d_cadena=nombres_demandantes
        self.cantidades_o_cadena=cantidades_ofertantes
        self.cantidades_d_cadena=cantidades_demandantes
        self.costos_unitarios=costos_unitarios
    
    #El procesamiento de los problemas de transportes son más ágiles al ser
    #un tipo particular de los mismos, en consecuencia para ello se busca definir
    #diccionarios, estos diccionarios almacenan tanto la oferta  y demanda máxima que puede enviar y solicitar un distribuidor y cliente respectivamente
    
    def diccionario_cantidades(self,lista_nombres_parametro,cantidad_parametro):
        #la función recibe una lista de nombres que ha de servir como key y el valor es proporcionado por las cantidades respectivas
        #como ambas listas poseen una misma longitud podemos recorrerlas
        #como las cantidades son una cadena debemos de transformarlas a listas
        cantidades=cantidad_parametro.split(",")
        #parseamos las cantidades a flotantes
        cantidades=[float(x) for x in cantidades]
        #cantidades es la misma longitud que los nombres, entonces retornamos un diccionario
        return dict(zip(lista_nombres_parametro,cantidades))

    def costos(self):
        #los costos deben tener la siguiente configuracion [[],[],...[]], es decir una lista de listas
        #los costos unitarios llegan separados cada ";" y luego en comas; entonces:
        costos_lista_de_listas=[]
        self.costos_unitarios=self.costos_unitarios.split(";") #lo convertimos en una lista de cadenas, ahora debemos de recorrer dichas cadenas
        for cadena in self.costos_unitarios:
            costos_lista_de_listas.append([int(x) for x in cadena.split(",")])
        return costos_lista_de_listas
    
    def procesar(self):
        #obtenemos los nombres como una cadena, y almacenamos como una lista, ya que serán usados en la creación
        #de los diccionarios, necesamos los nombres de los ofertantes y demandantes
        lista_o_nombres=self.nombres_o_cadena.split(",")
        lista_d_nombres=self.nombres_d_cadena.split(",")
        #creamos un diccionario de ofertas y demandas
        diccionario_demanda_cantidad=self.diccionario_cantidades(lista_d_nombres,self.cantidades_d_cadena)
        diccionario_oferta_cantidad=self.diccionario_cantidades(lista_o_nombres,self.cantidades_o_cadena)
        costos_lista_de_listas=self.costos()
        resolucionador=Resolucionador(lista_o_nombres,lista_d_nombres,diccionario_oferta_cantidad,diccionario_demanda_cantidad,costos_lista_de_listas)
        respuestas=resolucionador.resolver_problema()
        return respuestas
