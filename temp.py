x = [0, 0, 0, 0, 0, 0, 9]
'''
s = 0

for i in range(len(x)):
    for j in range(i+1,len(x)):
        s += abs(x[j] - x[i])
        print(x[i], x[j], abs(x[j] - x[i]))

print(s)


o = len(x)-1
i = o - 1
assigned = True

while assigned:
    assigned = False
    o = len(x) - 1
    i = o - 1
    while i >= 0:
        while x[o] - (x[i]+1) > 0:
            assigned = True
            x[i] += 1
            x[o] -= 1
            print(x)
        i -= 1
        o -= 1
'''


def compute_pattern():
    n = len(x)
    k = (n-1) * x[n-1]
    o = n - 1
    i = o - 1
    assigned = True
    print(x , k)
    debuglists = []

    while assigned:
        assigned = False
        debuglists.append((list(x),k))
        o = n - 1
        i = o - 1
        while i >= 0:
            while x[o] - (x[i] + 1) > 0:
                assigned = True
                x[i] += 1
                x[o] -= 1
                k -= 2
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
                print(x, k)
                assigned = True
                break
        debuglists.append((list(x), k))
    print(debuglists)
    for each in debuglists:
        dls, dkv = each[0], each[1]
        foc, soc = -1, -1
        if(dls[0] != 0): continue
        for z in range(n):
            if(dls[z] == 0):
                continue
            foc = z - 1
            break
        for z in range(foc, n):
            if(dls[z] > 1):
                soc = z
                break
        nkv = dkv - (soc - foc)*2
        print(dls,nkv)

compute_pattern()

x = [0, 0, 0, 0, 0, 0, 9]
print(x)

n = len(x)
o = n-1
i = o - 1
k = (n-1) * x[o]

assigned = True

while assigned:
    assigned = False
    while x[o] > x[o-1] and i >= 0:
        x[o] -= 1
        x[i] += 1
        k -= 2 * (o-i)
        i -= 1
        print(x, k)
    if x[o] > x[o-1]:
        assigned = True
        i = o - 1


prev = float('-inf')

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is not None:
            self.isValidBST(root.left)
            if root.val <= prev:
                return False
            prev = root.val
            self.isValidBST(root.right)
        return True