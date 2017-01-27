import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
points = [int(x_temp) for x_temp in input().strip().split(' ')]

points.sort()
# list of transmitters
t = []
# start
s = 0
# next
f = s + 1

while True:
    if s >= n-1:
        if s == n-1:
            t.append(points[s])
        break
    f = s + 1
    while f < n and points[f] - points[s] <= k:
        f += 1
    s = f - 1
    t.append(points[s])
    while f < n and points[f] - points[s] <= k:
        f += 1
    s = f

print(len(t))


'''
if n == 1:
    print(points[0])
else:
    while True:
        if start_p == n:
            transmitters.append(points[start_p])
            break
        if points[next_p] - points[start_p] > k:
            transmitters.append(points[start_p])
            start_p = next_p
            next_p = start_p + 1
        else:
            while n > next_p and points[next_p] - points[start_p] <= k:
                next_p += 1
            start_p = next_p - 1
            transmitters.append(points[start_p])
            while n > next_p and not points[next_p+1] - points[start_p] > k:
                next_p += 1
            start_p = next_p + 1
            next_p = start_p + 1

'''