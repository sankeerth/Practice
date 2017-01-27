class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

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
    # @param root, a tree link node
    # @return nothing
    def join_neighbor(self, temp, child):
        while temp.next:
            if temp.next.left:
                child.next = temp.next.left
                break
            elif temp.next.right:
                child.next = temp.next.right
                break
            temp = temp.next

    def connect(self, root):
        # return if node is null or if it is a leaf node
        if root is None or root.left is None and root.right is None:
            return

        # check if node has both children
        if root.left and root.right:
            root.left.next = root.right
            self.join_neighbor(root, root.right)
        elif root.left:
            self.join_neighbor(root, root.left)
        elif root.right:
            self.join_neighbor(root, root.right)

        self.connect(root.right)
        self.connect(root.left)


r = deserialize('[0,1,2,3,null,5,6,9,null,null,10,7,8]')
s = Solution()
s.connect(r)
