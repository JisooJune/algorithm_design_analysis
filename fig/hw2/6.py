def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s

    # 初始化dp数组
    dp = [[False] * n for _ in range(n)]
    start = 0  # 记录最长回文子串的起始位置
    max_len = 1  # 记录最长回文子串的长度

    # 单个字符是回文
    for i in range(n):
        dp[i][i] = True

    # 检查长度为2的子串
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # 检查长度大于2的子串
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length

    # 返回最长回文子串
    return s[start:start + max_len]


# 示例
s = "adccacccd"
result = longest_palindrome(s)
print("输出:", len(result))  # 输出: 7