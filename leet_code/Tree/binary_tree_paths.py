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


class Solution:
    def __init__(self):
        self.iter = list()
        self.res = list()

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is not None:
            self.iter.append(str(root.val))
            if root.left is None and root.right is None:
                self.res.append("->".join(self.iter))
            self.binaryTreePaths(root.left)
            self.binaryTreePaths(root.right)
            self.iter.pop()
        return self.res

s = Solution()
r = deserialize('[1,2,3,null,5]')
print(s.binaryTreePaths(r))
