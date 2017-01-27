from collections import defaultdict


def findItinerary(tickets):
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    print(sorted(tickets)[::-1])
    #targets['JFK'].sort()
    print(targets)
    visit('JFK')
    return route[::-1]


def visit(airport):
    while targets[airport]:
        visit(targets[airport].pop())
    route.append(airport)


route = []
targets = defaultdict(list)
tickets = [["JFK","A"], ["JFK","D"], ["A","C"],["B","C"], ["C","D"], ["C","JFK"],["D","A"], ["D","B"]]
print(findItinerary(tickets))