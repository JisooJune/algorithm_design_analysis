def majority_element_sort(nums):
    nums.sort()
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count > len(nums) // 2:
            return nums[i]
    return None

# 示例
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element_sort(nums1))  # 输出: 3
print(majority_element_sort(nums2))  # 输出: 2


def majority_element_moore(nums):
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # 验证 candidate1 和 candidate2 是否确实是多数元素
    if nums.count(candidate1) > len(nums) // 2:
        return candidate1
    if nums.count(candidate2) > len(nums) // 2:
        return candidate2
    return None


# 示例
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element_moore(nums1))  # 输出: 3
print(majority_element_moore(nums2))  # 输出: 2