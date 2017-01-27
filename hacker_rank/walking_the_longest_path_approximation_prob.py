n, m = map(int, input().strip().split())
from collections import Counter, defaultdict
adjls = defaultdict(list)
cntr = Counter()
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
nodes = []
for i in range(n):
    nodes.append(Node(i+1))
for _ in range(m):
    a, b = map(int, input().strip().split())
    adjls[a].append(nodes[b-1])
    adjls[b].append(nodes[a-1])

depth = 0
visited = [0 for i in range(n)]

for k,v in adjls.items():
    print(k)
    for e in v:
        print(e.value, end='')
    print('')

for i in nodes:
    print(i.parent)

def dfs():

