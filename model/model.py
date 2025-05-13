from collections import Counter

import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    @staticmethod
    def getColori():
        return DAO.getColori()

    def buildGraph(self, anno, colore):
        self._graph.clear()
        nodi = DAO.getProdotti(colore)
        self._graph.add_nodes_from(nodi)
        for nodo in nodi:
            self._idMap[nodo.Product_number] = nodo
        vendite = DAO.getVendite(anno, self._idMap)
        for vendita in vendite:
            if self._graph.has_edge(self._idMap[vendita["p1"]], self._idMap[vendita["p2"]]):
                pesoAttuale = self._graph[self._idMap[vendita["p1"]]][self._idMap[vendita["p2"]]]["weight"]
                self._graph[self._idMap[vendita["p1"]]][self._idMap[vendita["p2"]]]["weight"] = pesoAttuale + 1
            else:
                self._graph.add_edge(self._idMap[vendita["p1"]], self._idMap[vendita["p2"]], weight = 1)

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getArchiPesoMaggiore(self):
        pesi = self._graph.edges(data="weight")
        top3 = sorted(pesi, key=lambda x: x[2], reverse=True)[:3]
        nodi = []
        for u, v, weight in top3:
            nodi.append(u)
            nodi.append(v)
        conteggi = Counter(nodi)
        duplicati = [elem for elem, count in conteggi.items() if count >1]
        return top3, duplicati

    def getNodi(self):
        return self._graph.nodes
