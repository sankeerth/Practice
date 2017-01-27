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
    def __init__(self):
        self.res = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #self.findMaxPath(root)
        self.findMaxPath2(root)
        return self.res

    def findMaxPath(self, root):
        """Find the path in the tree that leads to maximum sum of the value at nodes.
        start node and end node of the patch can be anywhere in the tree and not just at the root.
        do a post order traversal of the tree and update the result (max sum path) if the path of
        left subtree to root to right subtree is greater than the result. key thing is to return the path
        that is maximum i.e. just the root or the left subtree and root or the right subtree and root."""

        if root is None:
            return 0
        l = self.findMaxPath(root.left)
        r = self.findMaxPath(root.right)

        if l + r + root.val > self.res:
            self.res = l + r + root.val
        if l + root.val > self.res:
            self.res = l + root.val
        if r + root.val > self.res:
            self.res = r + root.val
        if root.val > self.res:
            self.res = root.val

        # print root.val, l, r, self.res
        max_sum = root.val
        if max_sum < root.val + l:
            max_sum = root.val + l
        if max_sum < root.val + r:
            max_sum = root.val + r

        return max_sum

    def findMaxPath2(self, root):
        """a simpler solution from leetcode. essentially the same but less conditions.
        this is because if l or r is nagative then we do not have to consider that as it
        only lowers the result and the returned value. instead of eliminating it with the conditions
        in the above solution, it can be ignored"""

        if root is None:
            return 0
        l = self.findMaxPath2(root.left)
        r = self.findMaxPath2(root.right)

        if l < 0:
            l = 0
        if r < 0:
            r = 0
        if l + r + root.val > self.res:
            self.res = l + r + root.val
        return max(l,r) + root.val

s = Solution()
r = deserialize('[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]')
print(s.maxPathSum(r))