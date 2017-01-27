text = "ababab"
#text = "abcdabcd"


def string_formation_from_substring(text):
    str_len = len(text)
    max_search_len = str_len >> 1

    for i in range(1, max_search_len+1):
        print(str_len, i)
        if str_len % i == 0:
            pattern = text[:i]
            print(pattern)
            if substring_search(text, str_len - i, pattern, i):
                return True
    return False


def substring_search(text, rem_str_len, pattern, pattern_len):
    str_i = pattern_len
    while rem_str_len > 0:
        for j in range(pattern_len):
            if pattern[j] != text[str_i]:
                return False
            str_i += 1
        rem_str_len -= pattern_len
    return True


string_formation_from_substring(text)

