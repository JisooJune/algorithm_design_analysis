# import random
#
# def quicksort(A, p, r):
#     if p < r:
#         q = partition(A, p, r)
#         quicksort(A, p, q - 1)
#         quicksort(A, q + 1, r)
#
# def partition(A, p, r):
#     # 随机选择三个元素并取中位数作为枢轴
#     mid = (p + r) // 2
#     pivot_index = random.choice([p, mid, r])
#     A[pivot_index], A[r] = A[r], A[pivot_index]
#     pivot = A[r]
#     i = p - 1
#     for j in range(p, r):
#         if A[j] < pivot:
#             i += 1
#             A[i], A[j] = A[j], A[i]
#     A[i + 1], A[r] = A[r], A[i + 1]
#     return i + 1
#
# # 示例
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 16, 14]
# k = 4
# quicksort(arr, 0, len(arr) - 1)
# print("排序后的数组:", arr)


def reorder_array(A, k):
    n = len(A)
    if n <= k:
        return sorted(A)

    block_size = n // k
    blocks = [A[i:i + block_size] for i in range(0, n, block_size)]

    for block in blocks:
        block.sort()

    result = []
    indices = [0] * k

    while len(result) < n:
        min_val = float('inf')
        min_block = -1

        for i in range(k):
            if indices[i] < len(blocks[i]) and blocks[i][indices[i]] < min_val:
                min_val = blocks[i][indices[i]]
                min_block = i

        result.append(min_val)
        indices[min_block] += 1

    return result


# 示例用法
A = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 16, 14]
k = 4
result = reorder_array(A, k)
print("Reordered array:", result)

import heapq


def find_first_k_smallest(A, k):
    if k == 0:
        return []

    max_heap = []
    for num in A:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -num)
        else:
            if -num > max_heap[0]:
                heapq.heapreplace(max_heap, -num)

    return [-x for x in sorted(max_heap, reverse=True)]


# 示例用法
A = [13, 3, 7, 9, 11, 1, 15, 2, 8, 10, 12, 16, 14, 5]
k = 4
result = find_first_k_smallest(A, k)
print("The first", k, "smallest elements are:", result)