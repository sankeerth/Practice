from collections import defaultdict


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


def find_leaves_of_binary_tree(root):
    if not root:
        return -1
    left = find_leaves_of_binary_tree(root.left)
    right = find_leaves_of_binary_tree(root.right)
    cur_level = max(left, right) + 1
    res[cur_level].append(root.val)
    return cur_level


r = deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
res = defaultdict(list)
find_leaves_of_binary_tree(r)
print(res)