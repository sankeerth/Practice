def verify_preorder_bst(array):
    """Trick is to set the root once a value greater than the root
    appears in the preorder array. Elements from the stack are popped
    until the element lesser than the current element and the last element
    popped becomes the root. No element greater than the root must appear
    in the array"""

    stack = list()
    root = float('-inf')
    for value in array:
        if value < root:
            return False
        while len(stack) > 0 and stack[-1] < value:
            root = stack.pop()

        stack.append(value)

    return True


print(verify_preorder_bst([6,3,1,5,4,9,8,7,11,10,13]))
