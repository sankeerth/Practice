ans = 0

def num_of_possible_steps(n):
    global ans
    if n <= 0:
        return ans
    if n % 2 == 0:
        ans += 1
    if n% 3 == 0:
        ans += 1
    return num_of_possible_steps(n-1)

print(num_of_possible_steps(4))

ans = 0

def count_ways(n):
    global ans
    if n < 0:
        return 0
    if n == 0:
        return 1
    ans = count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
    return ans

print(count_ways(4))

ans = 0
res = [0] * 7
res[0] = 1
res[1] = 2
res[2] = 4

def count_ways_dp(n):
    for i in range(3, n):
        res[i] = res[i-1] + res[i-2] + res[i-3]
    return res[n-1]

print(count_ways_dp(6))