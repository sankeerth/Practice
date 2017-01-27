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


def course_schedule_2(graph):
    for s in graph.adj_list.keys():
        if not visited[s]:
            recur_stack = [False] * len(graph.adj_list)
            course_schedule_2_util(graph.adj_list, s, recur_stack)
    if is_cycle_present:
        stack.clear()

def course_schedule_2_util(adj_list, s, recur_stack):
    global is_cycle_present
    visited[s] = True
    recur_stack[s] = True
    for v in adj_list[s]:
        if recur_stack[v]:
            is_cycle_present = True
            return
        if not visited[v]:
            course_schedule_2_util(adj_list, v, recur_stack)
    recur_stack[s] = False
    stack.append(s)

g = Graph()

g.add_directed_edge(0, 1)
g.add_directed_edge(0, 3)
g.add_directed_edge(2, 1)
g.add_directed_edge(3, 2)


graph_size = len(g.adj_list)
visited = [False] * graph_size
is_cycle_present = False
stack = list()

print(g.adj_list)
course_schedule_2(g)
print(stack)


# Interesting solution from leetcode


def findOrder(numCourses, prerequisites):
    dic = defaultdict(set)
    neigh = defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    stack = [i for i in range(numCourses) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res if not dic else []

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))