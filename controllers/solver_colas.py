import ciw

class Resolucionador:
    def __init__(self,servidores,t_llegada,t_atencion,probabilidad,costo_atencion,costo_espera):
        self.servidores=servidores
        self.t_llegada=t_llegada
        self.t_atencion=t_atencion
    
    def resolucion(self):
        N=ciw.create_network(
            arrival_distributions=[ciw.dists.Exponential(self.t_llegada)],
            service_distributions=[ciw.dists.Exponential(self.t_atencion)],
            number_of_servers=[self.servidores]
        )
        ciw.seed(1)
        Q=ciw.Simulation(N)
        Q.simulate_until_max_time(1440)