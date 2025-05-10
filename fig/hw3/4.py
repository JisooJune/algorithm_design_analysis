def climb_stairs_optimized(n):
    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp

    return b


# 示例
n = 10
result = climb_stairs_optimized(n)
print("爬到第{}阶楼梯的方法数为: {}".format(n, result))