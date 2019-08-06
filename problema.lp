\* Problema de Transporte *\
Minimize
Función_Objetivo: 2 ruta_A_b1 + 4 ruta_A_b2 + 5 ruta_A_b3 + 2 ruta_A_b4
 + ruta_A_b5 + 3 ruta_B_b1 + ruta_B_b2 + 3 ruta_B_b3 + 2 ruta_B_b4
 + 3 ruta_B_b5
Subject To
Demandas_máximas_por_clientesb1: ruta_A_b1 + ruta_B_b1 >= 500
Demandas_máximas_por_clientesb2: ruta_A_b2 + ruta_B_b2 >= 900
Demandas_máximas_por_clientesb3: ruta_A_b3 + ruta_B_b3 >= 1800
Demandas_máximas_por_clientesb4: ruta_A_b4 + ruta_B_b4 >= 200
Demandas_máximas_por_clientesb5: ruta_A_b5 + ruta_B_b5 >= 700
Ofertas_máximas_por_distribuidor_A: ruta_A_b1 + ruta_A_b2 + ruta_A_b3
 + ruta_A_b4 + ruta_A_b5 <= 1000
Ofertas_máximas_por_distribuidor_B: ruta_B_b1 + ruta_B_b2 + ruta_B_b3
 + ruta_B_b4 + ruta_B_b5 <= 4000
Bounds
0 <= ruta_A_b1
0 <= ruta_A_b2
0 <= ruta_A_b3
0 <= ruta_A_b4
0 <= ruta_A_b5
0 <= ruta_B_b1
0 <= ruta_B_b2
0 <= ruta_B_b3
0 <= ruta_B_b4
0 <= ruta_B_b5
Generals
ruta_A_b1
ruta_A_b2
ruta_A_b3
ruta_A_b4
ruta_A_b5
ruta_B_b1
ruta_B_b2
ruta_B_b3
ruta_B_b4
ruta_B_b5
End
