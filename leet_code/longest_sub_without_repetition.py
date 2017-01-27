from collections import defaultdict

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    dictionary = defaultdict(int)
    cur_len = 0
    max_len = 0

    for i in range(len(s)):
        if not dictionary[s[i]]:
            dictionary[s[i]] = i+1
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = (i+1) - dictionary[s[i]]
            pos = dictionary[s[i]]
            dictionary = defaultdict(int)
            for j in range(pos, i+1):
                dictionary[s[j]] = j+1

    return max(cur_len, max_len)


print(lengthOfLongestSubstring("pwxwkew"))
