def counting_sort(strs, p):
    count = [0] * 27

    for s in strs:
        if p >= len(s):
            count[0] += 1
        else:
            count[ord(s[p]) - ord('a') + 1] += 1

    for i in range(1, 27):
        count[i] += count[i - 1]

    output = [None] * len(strs)

    for i in range(len(strs) - 1, -1, -1):
        if p >= len(strs[i]):
            index = 0
        else:
            index = ord(strs[i][p]) - ord('a') + 1
        output[count[index] - 1] = strs[i]
        count[index] -= 1

    for i in range(len(strs)):
        strs[i] = output[i]


def radix_sort_strs(strs):
    if not strs:
        return []

    max_len = max(len(s) for s in strs)

    for p in range(max_len - 1, -1, -1):
        counting_sort(strs, p)

    return strs


# A=["a", "da", "bde", "ab", "bc", "abdc", "cdba"]
A = ['ab', 'a', 'b', 'abc', 'ba', 'c']
print(radix_sort_strs(A.copy()))
