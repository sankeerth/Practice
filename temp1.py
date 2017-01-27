class Point:
    def __init__(self, index, t, v):
        self.idx = index
        self.v = v
        self.type = t

    def __cmp__(self, other):
        if None == other:
            return 1
        return self.v - other.v


def findOverlappedPairs(pairs):
    ls = []
    for idx, pair in enumerate(pairs):
        ls.append(Point(idx, 1, pair[0]))
        ls.append(Point(idx, 2, pair[1]))
    ls = sorted(ls, key=lambda x: x.v)
    count = 0
    prev = None
    for point in ls:
        if point.type == 1:
            if count > 0:
                if prev != None:
                    print(pairs[prev])
                    prev = None
                print(pairs[point.idx])
            else:
                prev = point.idx
            count += 1
        else:
            count -= 1


findOverlappedPairs([(1, 3), (12, 14), (2, 4), (13, 15), (5, 10)])