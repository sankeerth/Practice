from collections import defaultdict, deque

def delete_duplicates_from_string_lexographical(string):
    """delete the duplicate characters from the string and output the lexicographically
    smallest possible result of all possible results
    ex: input: cbacdcbc | output: acdb
    ex: input: bbbcaba | output: cab"""
    dict_char_count = defaultdict(int)
    low = s[0]

    # iterate the string to keep the count of the characters in the dict
    # also update 'low' to have the smallest character in string
    for c in string:
        dict_char_count[c] += 1
        if c < low:
            low = c

    # remove all the duplicate characters before start of the output string
    # start of the output string is either the lexicographically least character
    # or the character whose occurrence count is 1
    # this iteration stops after identifying the start of output string
    start = 0
    for c in string:
        if c is low or dict_char_count[c] == 1:
            break
        dict_char_count[c] -= 1
        start += 1

    # 'res' stores the output string (result)
    # 'is_added' is an array that stores if the character is added to the the result
    res = list()
    is_added = [0] * 26

    # iterate the string from the 'start' of the output string after removing duplicates before it
    # if the character is not added to the result, add it only if the next character is lexicographically
    # larger than the current character or if the count of the current character is 1
    for i in range(start, len(string)):
        c = string[i]
        if not is_added[ord(c) - 97]:
            if dict_char_count[c] == 1 or c < string[i+1]:
                res.append(c)
                is_added[ord(c) - 97] = 1
        dict_char_count[c] -= 1

    return ''.join(res)


s = "cbacdcbc"
#s = "bbbcaba"
print(delete_duplicates_from_string_lexographical(s))
