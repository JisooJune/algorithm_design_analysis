def find_local_min(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return A[left]

# 示例
A = [9, 3, 7, 2, 1, 4, 5]
print(find_local_min(A))

def find_all_local_minimum(A):
    n=len(A)
    local_minimums=[]
    if n>1 and A[0]<A[1]:
        local_minimums.append(A[0])
    for i in range(1,n-1):
        if A[i]<A[i-1] and A[i]<A[i+1]:
            local_minimums.append(A[i])
    if n>1 and A[n-1]<A[n-2]:
        local_minimums.append(A[n-1])
    return local_minimums

A=[9, 3, 7, 2, 1, 4, 5 ]
print("所有局部最小值为：",find_all_local_minimum(A))