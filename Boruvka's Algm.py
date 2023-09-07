"""
Implementing Boruvka's Algorithm for a graph represented by Adjacency List

self.graph --> Adjacency List : {A : [[B, 10], [C, 20]]}
self.edges --> {
                    [A, B] : 12,
                    [B, C] : 7
                }
"""


class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, edge_weight):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

        self.edges[vertex1, vertex2] = edge_weight
        self.edges[vertex2, vertex1] = edge_weight

    # to find the parent of the vertices so that we categorise into components
    # parent --> dict{[vertex] : parentVertex}

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        else:
            return self.find(parent, parent[vertex])

    def union(self, vertex1, vertex2, rank, parent):
        root1 = self.find(parent, vertex1)
        root2 = self.find(parent, vertex2)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    def borukov(self):
        #  initialising
        mst = []
        parent = {_: _ for _ in self.graph}
        rank = {_: 0 for _ in self.graph}
        cheapest = {_: 0 for _ in self.graph}
        num_components = len(self.graph)

        # while num_components > 1:


graph = Graph()
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

for i in vertices:
    graph.add_vertex(i)

graph.add_edge('a', 'b', 12)
graph.add_edge('a', 'd', 23)
graph.add_edge('a', 'k', 8)
graph.add_edge('b', 'c', 7)
graph.add_edge('b', 'f', 5)
graph.add_edge('c', 'j', 14)
graph.add_edge('d', 'e', 20)
graph.add_edge('d', 'g', 10)
graph.add_edge('e', 'h', 1)
graph.add_edge('f', 'i', 15)
graph.add_edge('f', 'j', 11)
graph.add_edge('g', 'k', 19)
graph.add_edge('h', 'k', 18)
graph.add_edge('h', 'm', 30)
graph.add_edge('i', 'm', 10)
graph.add_edge('j', 'n', 2)
graph.add_edge('k', 'l', 3)
graph.add_edge('l', 'h', 17)
graph.add_edge('m', 'n', 9)

print(graph.graph, end="\n\n")
print(graph.edges)
