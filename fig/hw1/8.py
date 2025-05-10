def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def find_k_smallest(arr, k):
    kth_smallest = quickselect(arr, k)
    return sorted(arr)[:k]

# 示例
arr = [5, 4, 3, 2, 6, 1, 88, 33, 22, 107]
k = 3
print("前{}个最小数据为：{}".format(k, find_k_smallest(arr, k)))

import heapq


def find_k_smallest_with_heap(arr, k):
    # 建立最小堆
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # 从堆中提取k个最小元素
    return sorted(min_heap)


# 示例
arr = [5, 4, 3, 2, 6, 1, 88, 33, 22, 107]
k = 3
print("前{}个最小数据为：{}".format(k, find_k_smallest_with_heap(arr, k)))





import random


def find_k_smallest_stream(arr, k):
    if k <= 0 or len(arr) == 0:
        return []

    # 随机抽取k个元素作为初始样本
    sample = sorted(random.sample(arr, min(k, len(arr))))

    # 初始化最小堆
    min_heap = []
    for num in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num < min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return sorted(min_heap)


# 示例
arr = [5, 4, 3, 2, 6, 1, 88, 33, 22, 107]
k = 3
print("前{}个最小数据为：{}".format(k, find_k_smallest_stream(arr, k)))