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
        self.res = list()
        self.level = 0

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.appendRightViewNodes(root, 0)
        return self.res

    def appendRightViewNodes(self, root, level):
        if root is not None:
            level += 1
            if level > self.level:
                self.level = level
                self.res.append(root.val)
            self.appendRightViewNodes(root.right, level)
            self.appendRightViewNodes(root.left, level)
        return self.res


s = Solution()
r = deserialize('[1,2,3,null,4,null,5,null,9,6,null,null,7,8,null,null,null,9,10,null,11,null,null,null,12]')
r = deserialize('[1,2,3,null,4,null,5,null,9,6,null,null,7,8,null,10,null,null,null,null,11,null,12,13,null,14,null,null,15]')
r = deserialize('[1,2,3,null,4,null,5,null,9,6,null,null,7,8,null,13,null,9,10,15,11,14,null,null,null,null,16,17,null,null,null,18,19,null,null,null,20,null,null,null,21]')

print(s.rightSideView(r))