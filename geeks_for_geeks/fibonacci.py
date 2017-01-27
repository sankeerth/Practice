num = 40

# top down approach (lazy learner as it does not calculate everything from 1 to n in certain instances)
result = [None for x in range(num + 1)]


def fib_td(n):
    if n <= 1:
        result[n] = n
    if result[n] is None:
        result[n] = fib_td(n - 1) + fib_td(n - 2)
    return result[n]


print(fib_td(num))
print(result)

# bottom up approach (not a lazy learner as it calculates everything from 1 to n in all instances)
result = [None for x in range(num + 1)]


def fib_bu(n):
    result[0] = 0
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[n]


print(fib_bu(num))
print(result)
