class Node:
    def __init__(self, label) -> None:
        self.label = label

    def __repr__(self) -> str:
        return f'{self.label}'


class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.adjancencyList = {}

    def addNode(self, label):
        node = Node(label)

        if label not in self.nodes:
            self.nodes[label] = node
        if node not in self.adjancencyList:
            self.adjancencyList[node] = []

    def addEdge(self, fromLabel, toLabel):
        fromNode = self.nodes[fromLabel]
        if fromNode is None:
            return
        toNode = self.nodes[toLabel]
        if toNode is None:
            return
        self.adjancencyList.get(fromNode).append(toNode)

    def removeNode(self, label):
        node = self.nodes.get(label)
        if node is None:
            return
        for k in self.adjancencyList.keys():
            destination = self.adjancencyList.get(k)
            if node in destination:
                destination.remove(node)
        self.adjancencyList.pop(node)
        if node in self.nodes:
            self.nodes.pop(node)

    def removeEdge(self, fromLabel, toLabel):
        fromNode = self.nodes.get(fromLabel)
        toNode = self.nodes.get(toLabel)

        if fromNode is None or toNode is None:
            return
        dest = self.adjancencyList.get(fromNode)
        if toNode in dest:
            self.adjancencyList.get(fromNode).remove(toNode)

    def print(self):
        for source, destination in self.adjancencyList.items():
            if len(destination) != 0:
                print(source, "is connected with", destination)


graph = Graph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")


graph.addEdge("A", "B")
graph.addEdge("A", "C")

graph.removeNode('A')

graph.print()
