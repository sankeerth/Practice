from collections import defaultdict

def countPairs(k, a):
    minimum = float("inf")
    digit_counts = defaultdict(int)
    for each in a:
        if each < minimum:
            minimum = each
        digit_counts[each] += 1

    cpairs = 0
    if k < minimum:
        return cpairs

    for a, b in digit_counts.items():
        kdash = k - a
        if kdash != a:
            cpairs += min(b, digit_counts[kdash])

    cpairs = cpairs // 2
    if k % 2 == 0:
        t = digit_counts[k // 2]
        if t > 1:
            cpairs += int((t * (t - 1)) / 2)

    return cpairs