import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    @staticmethod
    def getColori():
        return DAO.getColori()

    def buildGraph(self):
        pass