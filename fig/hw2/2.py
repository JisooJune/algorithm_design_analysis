def two_sum(nums, target):
    # 创建一个哈希表，存储数组元素及其索引
    num_dict = {}
    for i, num in enumerate(nums):
        # 计算与当前元素相加等于目标值的另一个元素
        complement = target - num
        # 如果另一个元素已经在哈希表中，则返回结果
        if complement in num_dict:
            return [num_dict[complement], i]
        # 将当前元素及其索引存入哈希表
        num_dict[num] = i

# 示例
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("输出:", result)  # 输出: [0, 1]