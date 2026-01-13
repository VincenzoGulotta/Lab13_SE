from math import inf

import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.peso_max = 0
        self.percorso = None

    def crea_grafo(self):
        cromosomi = DAO.get_cromosomi()
        for cromosoma in cromosomi:
            self.G.add_node(cromosoma)

    def crea_connessioni(self):
        lista_corr = DAO.get_correlazioni()
        for corr in lista_corr:
            cromosoma1 = corr[0]
            cromosoma2 = corr[1]
            peso = corr[2]
            if self.G.has_edge(cromosoma1, cromosoma2):
                self.G[cromosoma1][cromosoma2]['weight'] += peso
            else:
                self.G.add_edge(cromosoma1, cromosoma2, weight = peso)

        num_nodes, num_edges = self.conta_nodi_archi()
        minimo, massimo = self.trova_min_max()

        return num_nodes, num_edges, minimo, massimo

    def conta_nodi_archi(self):
        num_nodes = self.G.number_of_nodes()
        num_edges = self.G.number_of_edges()

        return num_nodes, num_edges

    def trova_min_max(self):
        minimo = float(inf)
        massimo = -1

        for edge in self.G.edges(data = True):
            weight = edge[2]['weight']
            if weight < minimo:
                minimo = weight
            elif weight > massimo:
                massimo = weight

        return minimo, massimo

    def conta_archi_soglia(self, soglia):
        counter_min = 0
        counter_max = 0
        for edge in self.G.edges(data = True):
            weight = edge[2]['weight']
            if weight < float(soglia):
                counter_min += 1
            elif weight > float(soglia):
                counter_max += 1

        return counter_min, counter_max

    def ricerca_percorso(self, soglia):
        self.peso_max = 0
        for node in self.G.nodes():
            self.ricorsione([],0,float(soglia),node)

        lista_percorso_peso = []
        for edge in self.percorso:
            node1 = edge[0]
            node2 = edge[1]
            peso = self.G[node1][node2]["weight"]
            lista = [node1, node2, peso]
            lista_percorso_peso.append(lista)

        return lista_percorso_peso, self.peso_max

    def ricorsione(self, percorso_parziale, peso_parziale, soglia, nodo):
        if peso_parziale > self.peso_max:
            self.peso_max = peso_parziale
            self.percorso = percorso_parziale

        for nuovo_nodo in self.G.neighbors(nodo):
            if self.G[nodo][nuovo_nodo]['weight'] > float(soglia):
                nuovo_arco = [nodo, nuovo_nodo]

                if nuovo_arco in percorso_parziale:
                    continue
                else:
                    nuovo_percorso = list(percorso_parziale)
                    nuovo_percorso.append(nuovo_arco)
                    peso = self.G[nodo][nuovo_nodo]['weight']
                    self.ricorsione(nuovo_percorso, peso_parziale + peso, soglia, nuovo_nodo)



















