text = "baaabab"
pattern = "*****ba*****ab"

text_len = len(text)
pattern_len = len(pattern)

def lcs():
    i = 0
    j = 0

    for i in range(len(text)):
        if j == (len(pattern)-1):
            if pattern[j] == '*':
                return True
            elif pattern[j] == '?':
                if i == (len(text)-1):
                    return True
                else:
                    return False
        if pattern[j] == '*':
            j += 1
        elif pattern[j] == '?':
            i += 1
            j += 1
        elif text[i] == pattern[j]:
            if i == (len(text)-1):
                return True
            i += 1
            j += 1
        else:
            return False

print(lcs())