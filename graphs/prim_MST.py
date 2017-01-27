from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_undirected_edge(self, src, dest, weight=0):
        self.adj_list[src].append((dest, weight))
        self.adj_list[dest].append((src, weight))

    def add_directed_edge(self, src, dest, weight=0):
        self.adj_list[src].append((weight, dest))
        if not self.adj_list[dest]:
            pass


def prim_MST(graph, s):
    """Prim's Minimum spannning Tree based on Heap"""
    heap = []
    distance[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        src = heapq.heappop(heap)[1]
        adj = graph.adj_list[src]
        visited[src] = True
        for node in adj:
            if not visited[node[1]]:
                if node[0] < distance[node[1]]:
                    distance[node[1]] = node[0]
                    parent[node[1]] = src
                    heapq.heappush(heap, node)


g = Graph()

g.add_directed_edge(0, 1, 4)
g.add_directed_edge(0, 7, 8)
g.add_directed_edge(1, 2, 8)
g.add_directed_edge(1, 7, 11)
g.add_directed_edge(2, 3, 7)
g.add_directed_edge(2, 5, 4)
g.add_directed_edge(2, 8, 2)
g.add_directed_edge(3, 4, 9)
g.add_directed_edge(3, 5, 14)
g.add_directed_edge(4, 5, 10)
g.add_directed_edge(5, 6, 2)
g.add_directed_edge(6, 7, 1)
g.add_directed_edge(6, 8, 6)
g.add_directed_edge(7, 8, 7)

graph_size = len(g.adj_list)
visited = [False] * graph_size
distance = defaultdict(float)
parent = defaultdict(int)

for k in g.adj_list.keys():
    distance[k] = float('inf')

prim_MST(g, 0)
print(distance)
print(parent)

print(g.adj_list)
