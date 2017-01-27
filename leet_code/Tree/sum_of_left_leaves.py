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


def sum_of_left_leaves(root, is_left=False):
    global res
    if root is not None:
        sum_of_left_leaves(root.left, True)
        if root.left is None and root.right is None and is_left:
            res += root.val
        sum_of_left_leaves(root.right, False)


r = deserialize('[3,9,20,null,null,15,7]')
r = deserialize('[6,2,9,1,3,7,10,null,null,null,4,null,null,null,11]')
res = 0
sum_of_left_leaves(r)
print(res)

