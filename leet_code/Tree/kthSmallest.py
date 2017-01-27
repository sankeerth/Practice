class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution(object):
    """Recursive solution"""
    def __init__(self):
        self.res = None
        self.found = False
        self.iter = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is not None and not self.found:
            self.kthSmallest(root.left, k)
            self.iter += 1
            if self.iter == k:
                self.res = root.val
                self.found = True
            self.kthSmallest(root.right, k)
        return self.res

    def kth_smallest(self, root, k):
        global index, found, ans
        if root:
            if not found:
                self.kth_smallest(root.left, k)
            index += 1
            if index == k:
                ans = root.val
                found = True
            if not found:
                self.kth_smallest(root.right, k)


r = deserialize('[6,2,8,0,4,7,10,null,null,3,5,null,null,9,11]')
s = Solution()

index, found, ans = 0, False, 0
s.kth_smallest(r, 3)
print(ans)


class Solution(object):
    """Iterative solution"""
    def __init__(self):
        self.res = None
        self.iter = 0
        self.stack = list()

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        while root is not None or self.stack:
            while root:
                self.stack.append(root)
                root = root.left
            root = self.stack.pop()
            self.iter += 1
            if self.iter == k:
                self.res = root.val
                break
            root = root.right

        return self.res

print(s.kthSmallest(r, 4))