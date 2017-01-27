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



def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.val, end=' ')
        in_order(root.right)


class Codec:
    def serialize(self, root):
        res = ""
        stack = list()
        stack.append(root)
        if root is None:
            return  None

        while stack:
            root = stack.pop()
            res += str(root.val)
            res += ","
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        print(res)
        return res

    def deserialize(self, data):
        root = None
        if data is None:
            return None
        data = data.split(',')
        data.pop()
        print(data)
        for val in data:
            print(val, end=' ')
            root = self.bst_insert(root, int(val))
        return root

    def bst_insert(self, root, data):
        if root is None:
            root = TreeNode(data)
        elif root.val > data:
            root.left = self.bst_insert(root.left, data)
        elif root.val < data:
            root.right = self.bst_insert(root.right, data)
        else:
            root.val = data
        return root

r = deserialize('[6,3,11,null,null,8,null,7,10,null,null,9]')
codec = Codec()
s = codec.deserialize(codec.serialize(r))
print()
in_order(s)


"""
OR this one that is better!


class Codec:

    def serialize(self, root):
        def pre_order(r):
            if r is not None:
                res.append(str(r.val))
                pre_order(r.left)
                pre_order(r.right)
        res = list()
        pre_order(root)
        return ' '.join(res)

    def deserialize(self, data):
        root = None
        data = map(int, data.split())
        for val in data:
            root = self.bst_insert(root, val)
        return root

    def bst_insert(self, root, data):
        if root is None:
            root = TreeNode(data)
        elif root.val > data:
            root.left = self.bst_insert(root.left, data)
        elif root.val < data:
            root.right = self.bst_insert(root.right, data)
        else:
            root.val = data
        return root

"""