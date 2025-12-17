from math import inf

import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.cromosomi = DAO.get_cromosomi()        # Lista di cromosomi - funziona
        self.interazioni = DAO.get_interazioni()    # Lista di oggetti Interazione - funziona

    def crea_grafo(self):
        for item in self.interazioni:
            cromosoma_1 = item.cromosoma_1
            cromosoma_2 = item.cromosoma_2
            correlazione = item.correlazione
            if self.G.has_edge(cromosoma_1, cromosoma_2):
                self.G[cromosoma_1][cromosoma_2]['weight'] += correlazione
            else:
                self.G.add_edge(cromosoma_1, cromosoma_2, weight = correlazione)

        num_nodes = self.G.number_of_nodes()
        num_edges = self.G.number_of_edges()
        max_weight = -1
        min_weight = float(inf)
        for edge in self.G.edges(data=True):
            if edge[2]['weight'] > max_weight: # edge : (gene1, gene2, {'weight': float})])
                max_weight = edge[2]['weight']
            if edge[2]['weight'] < min_weight:
                min_weight = edge[2]['weight']

        return num_nodes, num_edges, max_weight, min_weight
        # TERMINATO FUNZIONA

    def conta_edges(self, soglia):
        counter_minus = 0
        counter_plus = 0
        for edge in self.G.edges(data=True):
            if edge[2]['weight'] > soglia:
                counter_plus += 1
            elif edge[2]['weight'] < soglia:
                counter_minus += 1

        return counter_minus, counter_plus













