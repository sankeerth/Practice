class Tree(object):
    """structure of the tree"""
    def __init__(self, d = None, l = None, r = None):
        self.data = d
        self.left = l
        self.right = r


def bst_insert(root, data):
    """traverse the tree and insert the data when the condition is met"""
    if root is None:
        root = Tree(d=data)
    elif data > root.data:
        root.right = bst_insert(root.right, data)
    else:
        root.left = bst_insert(root.left, data)
    return root


def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if isBalancedUtil(root) == -1:
        return False
    else:
        return True


def isBalancedUtil(root):
    if root is None:
        return 0

    lh = isBalancedUtil(root.left)
    if lh == -1:
        return -1
    rh = isBalancedUtil(root.right)
    if rh == -1:
        return -1

    if abs(lh - rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            h, res = self.isBalancedUtil(root)
            return res

    def isBalancedUtil(self, root):
        if root is None:
            return 0, True

        lh, l = self.isBalancedUtil(root.left)
        rh, r = self.isBalancedUtil(root.right)

        if l and r and abs(lh - rh) < 2:
            return max(lh, rh) + 1, True
        else:
            return max(lh, rh) + 1, False

root = bst_insert(None, 4)
bst_insert(root, 2)
bst_insert(root, 6)
bst_insert(root, 1)
bst_insert(root, 3)
bst_insert(root, 5)
bst_insert(root, 7)

print(isBalanced(root))