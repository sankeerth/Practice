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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

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
res = s.lowestCommonAncestor(r, r.left.left, r.left.right.right)
print(res.val)

index, found, ans = 0, False, 0
s.kth_smallest(r, 3)
print(ans)