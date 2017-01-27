# not yet solved!

def shortest_palindrome(s):
    res = list()
    i, j = 0, len(s) - 1

    while i != j and i < j:
        if s[i] == s[j]:
            res.append(s[i])
            i += 1
            j -= 1
        else:
            res.append(s[j])
            while i > 0:
                if s[i-1] == s[j]:
                    break
                i -= 1
            j -= 1

    while i < len(s):
        res.append(s[i])
        i += 1

    return ''.join(res)


print(shortest_palindrome("ababbbabbaba"))
