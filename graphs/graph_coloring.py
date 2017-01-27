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


def graph_coloring(graph, num_colors=2):
    """This ensures that no adjacent vertices have the same color
    When colors are 2, it is a bipartite problem"""

    colors = [i for i in range(num_colors)]
    node_color = [None] * graph_size

    for s in graph.adj_list.keys():
        if not visited[s]:
            node_color[s] = 0
            if not graph_coloring_util(graph.adj_list, s, node_color, num_colors):
                print("Coloring not possible for this graph for node starting: ", s)

    return node_color


def graph_coloring_util(adj_list, s, node_color, num_colors):
    visited[s] = True
    for v in adj_list[s]:
        if not visited[v]:
            if not node_color[v]:
                node_color[v] = (node_color[s] + 1) % num_colors
                graph_coloring_util(adj_list, v, node_color, num_colors)
        elif node_color[v] == node_color[s]:
            return False
    return True

g = Graph()

g.add_undirected_edge(0, 1)
g.add_undirected_edge(1, 2)
g.add_undirected_edge(2, 3)
g.add_undirected_edge(3, 4)
g.add_undirected_edge(4, 5)
g.add_undirected_edge(5, 0)

graph_size = len(g.adj_list)
visited = [False] * graph_size

print(g.adj_list)

colors = graph_coloring(g)
print(colors)


g = Graph()

g.add_undirected_edge(0, 1)
g.add_undirected_edge(1, 2)
g.add_undirected_edge(2, 3)
g.add_undirected_edge(3, 4)
g.add_undirected_edge(4, 0)

graph_size = len(g.adj_list)
visited = [False] * graph_size

print(g.adj_list)

colors = graph_coloring(g)
g.adj_list.pop(1)
print(g.adj_list)
print(colors)
