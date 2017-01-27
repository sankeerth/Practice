from collections import defaultdict

# Graph implementation using class in python (not just representing next nodes in a list)
# This is as per my github representation in C++


class Node:
    # class to represent each node/vertice in the graph
    def __init__(self, src=None, dest=None, weight=0, next=None):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.next = next


class List:
    # class for adjacency list representation in the graph
    def __init__(self, head=None):
        self.head = head


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(List)

    def add_undirected_edge(self, src, dest, weight=0):
        # adds an undirected edge from 'src' to 'dest' and
        # from 'dest' to 'src'
        new_node = Node(src, dest, weight)
        new_node.next = self.adj_list[src].head
        self.adj_list[src].head = new_node

        new_node = Node(dest, src, weight)
        new_node.next = self.adj_list[dest].head
        self.adj_list[dest].head = new_node

    def add_directed_edge(self, src, dest, weight=0):
        # adds a directed edge from 'src' to 'dest'
        new_node = Node(src, dest, weight)
        new_node.next = self.adj_list[src].head
        self.adj_list[src].head = new_node

        if not self.adj_list[dest].head:
            pass

    def get_node_count(self):
        # returns the numbers of nodes/vertices in the graph
        return len(self.adj_list)

    def get_node(self, src):
        # returns the node given by the src
        return self.adj_list[src].head

g = Graph()
#g.add_undirected_edge(0, 1)
#g.add_undirected_edge(0, 2)

g.add_directed_edge(5, 2)
g.add_directed_edge(5, 0)
g.add_directed_edge(4, 0)
g.add_directed_edge(4, 1)
g.add_directed_edge(2, 3)
g.add_directed_edge(3, 1)

src = g.get_node(0)

# to traverse through the adj list of a particular node
while src is not None:
    print("src: ", src.src, "dest: ", src.dest)
    src = src.next

# Graph implementation using list as a contruct for default dict
# This implementation represents next nodes by the number of the node and not class


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

g = Graph()
g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
print(g.adj_list)

# Graph implementation using list as a contruct for default dict with weight
# This implementation represents next nodes by the number of the node and not class

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


g = Graph()
g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
print(g.adj_list)
