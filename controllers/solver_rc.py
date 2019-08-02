import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

import tkinter
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg,NavigationToolbar2Tk)


class Resolucionador:
    def __init__(self,nodos_lista_parametro,arcos_lista_parametro,frame_parametro):
        self.nodos_lista=nodos_lista_parametro
        self.arcos_lista=arcos_lista_parametro
        self.frame=frame_parametro
        self.G=nx.DiGraph()
    
    def obtener_arcos(self):
        #quizá pueda parecer que la función es muy vacía;sin embargo, da claridad al 
        # proyecto sobre que se obtiene con cada uno de los pasos
        self.G.add_edges_from(self.nodos_lista)

    def obtener_pesos_arcos(self):
        for i in range(len(self.arcos_lista)):
            self.G[self.nodos_lista[i][0]][self.nodos_lista[i][1]]["weight"]=self.arcos_lista[i]
    
    def obtener_posiciones(self):
        return nx.networkx.spring_layout(self.G)

    def obtener_ruta_critica_y_longitud(self):
        ruta=nx.algorithms.dag.dag_longest_path(self.G)
        longitud=nx.algorithms.dag.dag_longest_path_length(self.G)
        ruta_pintar=[]
        for i in range(len(ruta)-1,0,-1):
            tupla=(ruta[i-1],ruta[i])
            ruta_pintar.append(tupla)
        return ruta,longitud,ruta_pintar;

    def dibujar_red(self,pos_parametro,ruta_pintar_parametro):
        #referencia: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close
        plt.close("all")#iniciamos eliminando cualquier gráfico anterior que haya podido existir
        #desde el momento en que se genera el gráfico ya se está proporcionando data 
        nx.draw_networkx(self.G,pos_parametro,True,True)
        arcos=nx.get_edge_attributes(self.G,"weight")
        nx.draw_networkx_edge_labels(self.G,pos_parametro,arcos)
        nx.draw_networkx_edges(self.G,pos_parametro,ruta_pintar_parametro,width=1,alpha=1,edge_color="r")
        # desarrollo correspondiente a matplot
        #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html
        
        fig=plt.figure(1,dpi=100,figsize=[4,3])
        canvas=FigureCanvasTkAgg(fig,master=self.frame)
        canvas.get_tk_widget().grid(row=0,column=0,padx=5,pady=2)
        fig.canvas.draw()

    def resolucion(self):
        self.obtener_arcos()
        self.obtener_pesos_arcos()
        pos=self.obtener_posiciones()
        ruta,longitud,ruta_pintar=self.obtener_ruta_critica_y_longitud()
        self.dibujar_red(pos,ruta_pintar)
        return ruta,longitud