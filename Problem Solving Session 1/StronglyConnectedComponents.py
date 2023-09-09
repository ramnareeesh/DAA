# Given below is the algorithm for identifying Strongly connected components. Find the SCC for the given graph. Your
# implementation should have function which computes transpose of the graph and print the Graph transpose

def mysort(x):
    return x[1]
class Graph:
    def __init__(self):
        self.adList = {}  # direcrted unweighted graph
        self.preTime = {}
        self.postTime = {}

    def add_vertices(self, vertex):
        self.adList[vertex] =[]

    def add_edges(self, s_d_pair):
        self.adList[s_d_pair[0]].append(s_d_pair[1])

    def dfs(self, source, visited):
        global time
        self.preTime[source] = time
        time += 1
        visited.append(source)
        for neighbour in self.adList[source]:
            if  neighbour not in visited:
                self.dfs(neighbour, visited)

        self.postTime[source] = time
        time += 1

    def transpose(self, transpose):
        for i in self.adList:
            transpose.adList[i] = []
        for i in self.adList:
            for j in self.adList[i]:
                transpose.adList[j].append(i)

    def sorting_fin_time(self):
        vertices_list = list(self.postTime.items())
        vertices_list.sort(key=mysort, reverse=True)
        return vertices_list


graph = Graph()
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(1, 2), (2, 3), (1, 4), (4, 5), (5, 6), (6, 4), (4, 7), (7, 8), (8, 9), (9, 10), (10, 7 )]
for _ in vertices:
    graph.add_vertices(_)

for _ in edges:
    graph.add_edges(_)
print(graph.adList)
time = 1
graph.dfs(1, [])
print("Discovery time = ", graph.preTime)
print("Finish time = ", graph.postTime)

graph_transpose = Graph()
graph.transpose(graph_transpose)
print(graph_transpose.adList)

sorted_vertices = graph.sorting_fin_time()



