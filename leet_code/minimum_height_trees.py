from collections import defaultdict, deque


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


def minimum_height_trees(graph):
    """Returns the nodes whose height of the graph(tree) is minimum if chosen as the root
    Perform a bfs and store the level of the nodes (similar of height of the tree)
    Return the nodes, if chosen as the root, height of the tree will be minimum"""

    graph_size = len(graph.adj_list)  # num of nodes
    queue = list()  # used for bfs
    dq = deque()  # store the intermediate nodes and the max level reached
    dq.append((float('inf'), 0))
    res = list()  # to store the final result that is to be returned

    for s in graph.adj_list.keys():
        level = [0] * graph_size  # store the level of each node in the graph(tree)
        visited = [False] * graph_size  # to check if the node is already visited during bfs
        level[s] = 0
        queue.append(s)
        queue.append(None)  # appends None after each level. This helps is setting the level to the node accordingly
        i = 1  # index to count the level of the current node
        while queue:
            cur = queue.pop(0)
            if cur is None:  # increment the index if None is found in queue.
                i += 1
                continue
            visited[cur] = True
            for v in graph.adj_list[cur]:
                if not visited[v]:
                    queue.append(v)
                    level[v] = i
            if queue[0] is None:
                queue.append(None)
        if i <= dq[0][0]:  # if the highest level reached is lower than the lowest in the deque
            dq.append((i, s))  # append the level and the starting node
            while dq[0][0] > i:  # remove all the nodes with the level greater than the lowest level
                dq.popleft()

    for i in range(len(dq)):
        res.append(dq[i][1])
    return res


def minimum_height_trees_delete_leaves(graph):
    # Any connected graph who has n nodes with n-1 edges is a tree.
    # A path graph is a tree with two or more vertices that is not branched at all.
    """Return the node of the graph(tree) whose height of graph is minimum
    if chosen as the root node. Remove the leaves of the graph (tree) and update the
    edges of the graph(tree). Keep removing the leaves until 1 or 2 nodes is reached."""

    leaves = list()
    num_nodes = len(graph.adj_list)
    for s in graph.adj_list.keys():
        # append the leaves to a list
        if len(graph.adj_list[s]) == 1:
            leaves.append(s)

    while True:
        new_leaves = list()
        for v in leaves:
            # remove the leaves from the graph (tree)
            # done by just removing the edges from the graph
            u = graph.adj_list[v].pop()
            graph.adj_list[u].remove(v)
            num_nodes -= 1
            if len(graph.adj_list[u]) == 1:
                # check if the node becomes a leaf node after updating the graph
                new_leaves.append(u)
        if num_nodes <= 2:
            return new_leaves
        leaves = new_leaves


def minimum_height_trees_double_traversal(graph):
    """Perform bfs/dfs from any random node. Again perform bfs/dfs starting from the last node
     reached in the previous search until the first node in the previous search. Save all the nodes
     in a list and return the middle node('s) of the list"""


g = Graph()

g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
g.add_undirected_edge(0, 3)
g.add_undirected_edge(4, 3)
g.add_undirected_edge(5, 4)

print(minimum_height_trees(g))
#print(minimum_height_trees_delete_leaves(g))

print(g.adj_list)
