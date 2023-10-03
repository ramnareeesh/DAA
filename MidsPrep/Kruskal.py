import heapq


class Graph:
    def __init__(self):
        self.adList = {}
        self.edges = []
        self.weights = {}

    def add_vertex(self, vertex):
        self.adList[vertex] = []

    def add_edge(self, source, destination, weight):
        self.adList[source].append(destination)
        self.adList[destination].append(source)

        self.edges.append((weight, source, destination))

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, rank, parent, v1, v2):
        root1 = self.find(parent, v1)
        root2 = self.find(parent, v2)
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal(self):
        mst = []
        parent = {_: _ for _ in self.adList}
        rank = {_: 0 for _ in self.adList}

        priority = []
        for e in self.edges:
            heapq.heappush(priority, e)

        while priority:
            weight, popvertex, parentvertex = heapq.heappop(priority)
            if self.find(parent, popvertex) != self.find(parent, parentvertex):
                mst.append((popvertex, parentvertex, weight))
                self.union(rank, parent, popvertex, parentvertex)

        return mst


def main():
    graph = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    for v in vertices:
        graph.add_vertex(v)

    edges = [('a', 'b', 4), ('b', 'c', 8), ('c', 'd', 7), ('d', 'e', 9), ('e', 'f', 10),
             ('d', 'f', 14), ('c', 'f', 4), ('g', 'f', 2), ('c', 'i', 2), ('i', 'g', 6),
             ('h', 'g', 1), ('h', 'i', 7), ('h', 'b', 11), ('a', 'h', 8)]
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])

    print(graph.adList)
    print(graph.weights)

    print()
    print(graph.kruskal())


main()
