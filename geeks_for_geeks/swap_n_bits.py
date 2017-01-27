N = 28


def swap_n_bits(N, start, end, n):
    offset = (2 ** n) - 1
    first_set = offset << (start - 1) & N
    second_set = offset << (end - 1) & N

    diff = N ^ first_set ^ second_set

    first_set = first_set << (end - start)
    second_set = second_set >> (end - start)

    ans = diff | first_set | second_set
    return ans


print(swap_n_bits(N, 1, 4, 2))
