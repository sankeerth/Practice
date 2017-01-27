n = int(input())
val = list(map(int, input().split(' ')))
res = [-1 for z in range(n)]


def compute(i):
    if res[i] >= 0:
        return res[i]
    global n
    ans = 0
    r = n - i
    for p in range(i, n):
        if val[p] - (p - i) <= 0:
            ans += 1
    for q in range(i):
        if val[q] - (r + q) <= 0:
            ans += 1
    return ans

res[0] = compute(0)

def compute_nex_tand_prev(s):
    if res[(s-1)%n] != -1:
        res[(s-1)%n] = compute((s-1)%n)
    if res[(s + 1) % n] != -1:
        res[(s+1)%n] = compute((s+1)%n)

    if res[s] > res[s-1] and res[s] > res[s+1]:
        return s


#compute_nex_tand_prev(0)

for i in range(n):
    res[i] = compute(i)

print(res.index(max(res)))
print(res)
