array = [98, 23, 54, 12, 20, 7, 27]


def next_greater_element_in_array(array):
    """append the first element to the stack and start the traversal from second element
    if current element in lesser than the element on the top of the stack then add it to stack
    if the current element is greater than top of the stack, pop elements from stack until the
    top of the stack is greater than the current element
    push the current element to the top of the stack
    popped elements have next greater element in the array as the current element"""
    stack = list()
    stack.append(array[0])
    for i in range(1, len(array)):
        if array[i] < stack[-1]:
            stack.append(array[i])
        else:
            while array[i] > stack[-1]:
                print("next element greater than ", stack[-1], " is ", array[i])
                stack.pop()
            stack.append(array[i])
    while stack:
        print("next element greater than ", stack[-1], " is ", None)
        stack.pop()


next_greater_element_in_array(array)