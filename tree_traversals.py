tree = [10,5,-3,3,2,None,11,3,-2,None,1]
tree = [1, 2, 3, 4, 5, 6, 7, None, None, None, None]

def pre_order(root):
    if root < len(tree) and tree[root] != None:
        print(tree[root])
        left = 2*root+1
        right = 2*root+2
        pre_order(left)
        pre_order(right)

def in_order(root):
    if root < len(tree) and tree[root] != None:
        left = 2*root+1
        right = 2*root+2
        in_order(left)
        print(tree[root])
        in_order(right)

def post_order(root):
    if root < len(tree) and tree[root] != None:
        left = 2*root+1
        right = 2*root+2
        post_order(left)
        post_order(right)
        print(tree[root])

print("======")
print("Pre Order")
pre_order(0)
print("======")
print("In Order")
in_order(0)
print("======")
print("Post Order")
post_order(0)
