import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()
#nodos_arcos_pesos=[(1,2,30),(2,3,5),(2,4,14),(2,5,6),(3,4,10),(3,7,15),(4,6,8),(5,6,4),(6,7,2)]
"""
(1,2);(2,3);(2,4);(2,5);(3,4);(3,7);(4,6);(5,6);(6,7)
"""
nodos_arcos_pesos=[(1,2),(2,3),(2,4),(2,5),(3,4),(3,7),(4,6),(5,6),(6,7)]
arcos_pesos=[30,5,14,6,10,15,8,4,2]
G.add_edges_from(nodos_arcos_pesos)
for i in range(len(nodos_arcos_pesos)):
    G[nodos_arcos_pesos[i][0]][nodos_arcos_pesos[i][1]]["weight"]=arcos_pesos[i]
print(G.edges(data=True))

#G.add_weighted_edges_from(nodos_arcos_pesos)
pos=nx.networkx.spring_layout(G)#obtenemos las posiciones en forma de vector de cada uno de los nodos
lista_nodos=nx.nodes(G)
#nx.draw_networkx_nodes(G,pos)
#nx.draw(G)
ruta=nx.algorithms.dag.dag_longest_path(G)
consumo=nx.algorithms.dag.dag_longest_path_length(G)
print(ruta,consumo)

ruta_tupla_lista=[]

for i in range(len(ruta)-1,0,-1):
    tupla=(ruta[i-1],ruta[i])
    #print(tupla)
    ruta_tupla_lista.append(tupla)

print(ruta_tupla_lista)
nx.draw_networkx(G,pos,True,True)#dibuja las etiquetas de los nodos
arcos=nx.get_edge_attributes(G,"weight") #obtenemos el diccionario que contiene el peso de cada arco
#print(arcos)
nx.draw_networkx_edge_labels(G,pos,arcos)# se imprime el valor de etiqueta de cada arco
nx.draw_networkx_edges(G,pos,ruta_tupla_lista,width=1, alpha=1, edge_color='r')
plt.show()