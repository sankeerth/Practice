from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_undirected_edge(self, src, dest, weight=0):
        self.adj_list[src].append((dest, weight))
        self.adj_list[dest].append((src, weight))

    def add_directed_edge(self, src, dest, weight=0):
        self.adj_list[src].append((dest, weight))
        if not self.adj_list[dest]:
            pass


def longest_path_DAG(graph, s):
    """Longest path in Directed Acyclic Graph
    Distance is updated performing a DFS on the graph
    However, geeksforgeeks does it by creating a Topological sort first and then
    updating the distances (Need to know if this is correct as well!)"""
    for v in graph.adj_list[s]:
        if (distance[s] + v[1] > distance[v[0]]) or distance[v[0]] == float('-inf'):
            distance[v[0]] = distance[s] + v[1]
            longest_path_DAG(graph, v[0])


g = Graph()

g.add_directed_edge('r', 's', 5)
g.add_directed_edge('r', 't', 3)
g.add_directed_edge('s', 't', 2)
g.add_directed_edge('s', 'x', 6)
g.add_directed_edge('t', 'x', 7)
g.add_directed_edge('t', 'y', 4)
g.add_directed_edge('t', 'z', 2)
g.add_directed_edge('x', 'y', -1)
g.add_directed_edge('x', 'z', 1)
g.add_directed_edge('y', 'z', -2)

graph_size = len(g.adj_list)
visited = [False] * graph_size

distance = defaultdict(float)
for k in g.adj_list.keys():
    distance[k] = float('-inf')

distance['s'] = 0.0

longest_path_DAG(g, 's')

print(g.adj_list)
print(sorted(distance.items()))