A = [10, 5, 20, 15, 30]
B = [10, 15, 30, 20, 5]


def check_bst_same_without_building(A, B, n):
    # list to store elements of left and right subtrees
    left_A = []
    right_A = []
    left_B = []
    right_B = []

    # variables to store the length of the left and right subtrees
    l_a = 0
    r_a = 0
    l_b = 0
    r_b = 0

    # return if the length of the BST's is 0
    if n == 0:
        return True

    # return false if the root of the BST's differ
    if A[0] != B[0]:
        return False

    # return True if there is only one element in the tree
    if n == 1:
        return True

    # iterate through BST's to check the length of left and right subtrees and return false if they differ
    for i in range(1, n):
        if A[i] < A[0]:
            left_A.append(A[i])
            l_a += 1
        else:
            right_A.append(A[i])
            r_a += 1

        if B[i] < B[0]:
            left_B.append(B[i])
            l_b += 1
        else:
            right_B.append(B[i])
            r_b += 1

    if l_a != l_b or r_a != r_b:
        return False

    return check_bst_same_without_building(left_A, left_B, len(left_A)) and \
        check_bst_same_without_building(right_A, right_B, len(right_A))


print(check_bst_same_without_building(A, B, len(A)))