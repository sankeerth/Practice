from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_undirected_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def add_directed_edge(self, src, dest):
        self.adj_list[src].append(dest)
        if not self.adj_list[dest]:
            pass


def topological_sort(graph):
    for s in graph.adj_list.keys():
        if not visited[s]:
            topological_sort_util(graph.adj_list, s)


def topological_sort_util(adj_list, s):
    visited[s] = True
    for v in adj_list[s]:
        if not visited[v]:
            topological_sort_util(adj_list, v)
    stack.append(s)

g = Graph()

g.add_directed_edge(5, 2)
g.add_directed_edge(5, 0)
g.add_directed_edge(4, 0)
g.add_directed_edge(4, 1)
g.add_directed_edge(2, 3)
g.add_directed_edge(3, 1)


graph_size = len(g.adj_list)
visited = [False] * graph_size
stack = list()
topological_sort(g)

print(g.adj_list)
print(stack[::-1])