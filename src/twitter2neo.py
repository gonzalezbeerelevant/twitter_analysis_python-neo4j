from py2neo import Graph, Node, Relationship

class Twitter2Neo:

    def __init__(self):
        pass

    def createSession(self, uri, user, password):
        self.graph = Graph(uri, user=user, password=password)

    def runCypher(self, command):
        self.graph.run(command)