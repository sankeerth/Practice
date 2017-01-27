q = int(input())
n, s, kv = map(int, input().split(' '))
res = [0 for i in range(n)]
x = [0 for i in range(n)]
x[n-1] = s

def compute():
    n = len(x)
    k = (n-1) * x[n-1]
    if k == kv:
        return x
    o = len(x) - 1
    i = o - 1
    assigned = True
    print(x , k)

    while assigned:
        assigned = False
        o = len(x) - 1
        i = o - 1
        while i >= 0:
            while x[o] - (x[i] + 1) > 0:
                assigned = True
                x[i] += 1
                x[o] -= 1
                k -= 2
                if k == kv:
                    return x
                print(x, k)
            i -= 1
            o -= 1

    assigned = True

    while assigned:
        i = x.index(max(x))
        assigned = False
        for j in range(i, -1, -1):
            if x[i] - x[j] > 1:
                x[i] -= 1
                x[j] += 1
                k -= (i - j) * 2
                if k == kv:
                    return x
                print(x, k)
                assigned = True
                break


for i in range(q):
    if kv > (n-1) * s:
        print(-1)
    elif n % 2 != 0 and kv % 2 != 0:
        print(-1)
    elif s == 0 and kv != 0:
        print(-1)
    elif kv == 0 and s != 0:
        if s % n == 0:
            res = [s / n for j in range(n)]
        else:
            print(-1)
    else:
        print(compute())
