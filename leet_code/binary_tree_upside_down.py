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


def binary_tree_upside_down(root, parent = None):
    global res
    if root is not None:
        binary_tree_upside_down(root.left, root)
        if res is None:
            res = root
        root.left = parent.right if parent is not None else None
        root.right = parent if parent is not None else None


def pre_order(root):
    if root is not None:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

res = None
r = deserialize('[1,2,3,4,5]')
binary_tree_upside_down(r)
