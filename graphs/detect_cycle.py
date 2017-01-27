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


def detect_cycle(graph):
    for s in graph.adj_list.keys():
        if not visited[s]:
            recur_stack = [False] * graph_size
            detect_cycle_util(graph.adj_list, s, recur_stack)


def detect_cycle_util(adj_list, s, recur_stack):
    visited[s] = True
    recur_stack[s] = True
    cycle_list.append(s)

    for v in adj_list[s]:
        if recur_stack[v]:
            cycle_list.append(v)
            print("Cycle detected")
            print(cycle_list)
            cycle_list.pop()
        else:
            detect_cycle_util(adj_list, v, recur_stack)
    recur_stack[s] = False
    cycle_list.pop()


def detect_cycle_undirected(graph):
    for s in graph.adj_list.keys():
        if not visited[s]:
            if detect_cycle_undirected_util(graph.adj_list, s):
                print(cycle_list)
                return True


def detect_cycle_undirected_util(adj_list, s):
    visited[s] = True
    cycle_list.append(s)
    for v in adj_list[s]:
        if not visited[v]:
            parent[v] = s
            if detect_cycle_undirected_util(adj_list, v):
                return True
        elif parent[s] != v:
            print("cycle detected")
            return True
    cycle_list.pop()
    return False


g = Graph()
'''
g.add_directed_edge(0, 1)
g.add_directed_edge(0, 2)
g.add_directed_edge(1, 2)
g.add_directed_edge(2, 0)
g.add_directed_edge(2, 3)
g.add_directed_edge(3, 3)
'''

g.add_directed_edge(0, 1)
g.add_directed_edge(0, 3)
g.add_directed_edge(2, 1)
g.add_directed_edge(3, 2)

graph_size = len(g.adj_list)
print(g.adj_list)
visited = [False] * graph_size
parent = [None] * graph_size
cycle_list = list()
detect_cycle(g)

g = Graph()

g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
g.add_undirected_edge(0, 3)
g.add_undirected_edge(1, 2)
g.add_undirected_edge(3, 4)

graph_size = len(g.adj_list)
print(g.adj_list)
visited = [False] * graph_size
parent = [None] * graph_size
cycle_list = list()
detect_cycle_undirected(g)

