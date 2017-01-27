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
    def isPalindrome(self, nodes, count):
        n = count - 1
        for i in range(int(count / 2)):
            if nodes[i] != nodes[n - i]:
                return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        queue = list()
        nodes = list()

        queue.append(root)
        queue.append(None)
        count = 0

        while queue:
            current = queue.pop(0);
            if current is None:
                print(queue)
                print(count)
                if queue:
                    queue.append(None)
                if count % 2 != 0:
                    return False
                if not self.isPalindrome(nodes, count):
                    return False
                del nodes[:]
                count = 0
            else:
                if current.left is not None:
                    queue.append(current.left)
                    nodes.append(current.left.val)
                    count += 1
                else:
                    nodes.append(None)
                if current.right is not None:
                    queue.append(current.right)
                    nodes.append(current.right.val)
                    count += 1
                else:
                    nodes.append(None)
        return True


tree = "[1,2,2,null,3,3]"
tree = "[1,2,2,null,3,null,3]"

r = deserialize('[1,2,2,null,3,null,3]')
sol = Solution()
print(sol.isSymmetric(r))
