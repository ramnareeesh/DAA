class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Initialize distances from the source vertex to all other vertices as infinity
        distance = [float("inf")] * self.V
        distance[src] = 0

        # Relax all edges |V| - 1 times, where |V| is the number of vertices
        for _ in range(self.V - 1):
            print(_)
            for u, v, w in self.graph:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                print("Graph contains negative-weight cycle")
                return

        # Print the shortest distances
        self.print_solution(distance)

    def print_solution(self, distance):
        print("Vertex \tDistance from Source")
        for i in range(self.V):
            print(f"{i}\t{distance[i]}")


# Example usage:
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)
