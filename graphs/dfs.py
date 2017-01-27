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


def dfs(graph):
    for s in graph.adj_list.keys():
        if not visited[s]:
            dfs_util(graph.adj_list, s)


def dfs_util(adj_list, s):
    print(s)
    visited[s] = True
    for v in adj_list[s]:
        if not visited[v]:
            parent[v] = s
            dfs_util(adj_list, v)


g = Graph()

g.add_directed_edge(0, 1)
g.add_directed_edge(0, 2)
g.add_directed_edge(1, 2)
g.add_directed_edge(2, 0)
g.add_directed_edge(2, 3)
g.add_directed_edge(3, 3)
g.add_directed_edge(4, 5)
g.add_directed_edge(5, 6)
g.add_directed_edge(6, 4)

graph_size = len(g.adj_list)
visited = [False] * graph_size # to check if the node is visited
parent = [None] * graph_size  # to store the parent of each node

dfs(g)
#dfs_util(g.adj_list, 2)

print(parent)
print(g.adj_list)