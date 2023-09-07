# Drunken Donuts, a new wine-and-donuts restaurant chain, wants to build restaurants on many street corners with the
# goal of maximizing their total profit. The street network is described as an undirected graph G = (V, E),
# where the potential restaurant sites are the vertices of the graph. Each vertex u has a non-negative integer value
# pu, which describes the potential profit of site u. Two restaurants cannot be built on adjacent vertices (to avoid
# self competition). You are supposed to design an algorithm that outputs the chosen set U ⊆ V of sites that maximizes
# the total profit u∈U pu. First, for parts (a)–(c), suppose that the street network G is acyclic, i.e., a tree.

# (a) Consider the following “greedy” restaurant-placement algorithm: Choose the highest-profit vertex u0 in the tree (
# breaking ties according to some order on vertex names) and put it into U. Remove u0 from further consideration,
# along with all of its neighbors in G. Repeat until no further vertices remain. Give a counterexample to show that
# this algorithm does not always give a restaurant placement with the maximum profit.

# (b) Suppose that, in the absence of good market research, DD decides that all sites are equally good, so the goal is
# simply to design a restaurant placement with the largest number of locations. Give a simple greedy algorithm for
# this case, and prove its correctness.

def sorting_key(e):
    return e[1]  # e -> ('vertex', profit), function returns profit, used for sorting


class UndirectedGraph:
    def __init__(self):
        self.graph = {}
        self.vertex_profit = {}     # stores the potential profit of each vertex

    def add_vertices(self, vertex, potent_profit):
        self.graph[vertex] = []
        self.vertex_profit[vertex] = potent_profit

    def add_edge(self, vertex1, vertex2):
        # undirected graph implementation - 2 way edges
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def find_locations(self):  # solution for (a)
        u = []
        total_profit = 0
        # sorting in descending with key set to the potential profit unit
        list_vertices = list(self.vertex_profit.items())
        list_vertices.sort(key=sorting_key, reverse=True)

        while list_vertices:
            vertex, profit = list_vertices.pop(0)
            u.append((vertex, profit))
            total_profit += profit

            for neighbours in self.graph[vertex]:
                for i in list_vertices:
                    if i[0] == neighbours:
                        list_vertices.remove(i)
        print(u)
        print(total_profit)

    def find_locations_equal(self):  # solution for (b)
        u = []
        total_locations = 0
        list_vertices = []
        for _ in self.graph:
            list_vertices.append((_, len(self.graph[_])))
        # sorting in ascending with key set to no of neighbours
        list_vertices.sort(key=sorting_key)

        while list_vertices:
            vertex, no_neighbours = list_vertices.pop(0)
            u.append((vertex, self.vertex_profit[vertex]))
            total_locations += 1
            for neighbours in self.graph[vertex]:
                for i in list_vertices:
                    if i[0] == neighbours:
                        list_vertices.remove(i)
        print(u)
        print(total_locations)


def main():
    street_net = UndirectedGraph()
    vertices = [('A', 10), ('B', 10), ('C', 10), ('D', 12), ('E', 10)]
    for i in vertices:
        street_net.add_vertices(i[0], i[1])

    edges = [('A', 'B'), ('A', 'C'), ('C', 'E'), ('C', 'D')]
    for _ in edges:
        street_net.add_edge(_[0], _[1])

    street_net.find_locations()
    print()
    street_net.find_locations_equal()


main()
