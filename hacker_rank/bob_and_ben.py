g = int(input())

for i in range(g):
    t = int(input())
    m = []
    k = []
    for j in range(t):
        t1, t2 = map(int,(input().split(' ')))
        m.append(t1)
        k.append(t2)
    print(m, k)
