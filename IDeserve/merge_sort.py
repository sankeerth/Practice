A = [1,4,2,8,3,7,6,5]
A = [8,7,6,5,4,3,2,1]
B = [0] * len(A)
for i in range(len(A)):
    B[i] = A[i]


def merge_sort(array, aux, low, high):
    if low < high:
        mid = int(low + (high - low)/2)
        merge_sort(aux, array, low, mid)
        merge_sort(aux, array, mid+1, high)
        # this sub array is already sorted hence return
        #if array[mid] < array[mid+1]:
         #   return
        merge(aux, array, low, mid, high)


def merge_sort_bottom_up(array, aux, low, high):
    size = (high - low) + 1
    i = 1
    while i < size:
        j = 0
        while j < size - i:
            l = j
            m = j+i-1
            h = j+i+i-1
            merge(array, aux, j, j+i-1, min(j+i+i-1, size-1))
            j += i + i
        i += i


def merge(array, aux, low, mid, high):
    i = low
    j = mid + 1

    for k in range(low, high+1):
        if i <= mid and j <= high:
            if array[i] <= array[j]:
                aux[k] = array[i]
                i += 1
            else:
                aux[k] = array[j]
                j += 1
        elif i <= mid:
            aux[k] = array[i]
            i += 1
        elif j <= high:
            aux[k] = array[j]
            j += 1

merge_sort(A, B, 0, 7)
merge_sort_bottom_up(A, B, 0, 7)
print(A)