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


def bfs(graph, src):
    graph_size = len(graph.adj_list)
    visited = [False] * graph_size
    queue = list()

    queue.append(src) # ADT to store the nodes visited
    parent = [None] * graph_size # to store the parent of each node
    level = [None] * graph_size # to store the level of the node in the graph

    i = 0 # level is 0 initially
    level[src] = src, i # level of src is 0

    while queue:
        s = queue.pop(0)
        visited[s] = True
        print(s)

        i += 1
        for v in graph.adj_list[s]:
            if not visited[v]:
                level[v] = v, i
                parent[v] = s
                queue.append(v)

    print(parent)
    print(level)

g = Graph()

g.add_directed_edge(0, 1)
g.add_directed_edge(0, 2)
g.add_directed_edge(1, 2)
g.add_directed_edge(2, 0)
g.add_directed_edge(2, 3)
g.add_directed_edge(3, 3)

bfs(g, 2)

print(g.adj_list)
