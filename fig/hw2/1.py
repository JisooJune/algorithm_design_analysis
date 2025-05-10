class NodeList:
    def __init__(self, val=None, right=None):
        self.val = val
        self.right = right

def array_to_linked_list(arr):
    if not arr:
        return None
    head = NodeList(arr[0])
    current = head
    for value in arr[1:]:
        current.right = NodeList(value)
        current = current.right
    return head

def delete_duplicates(head):
    if not head or not head.right:
        return head
    current = head
    while current and current.right:
        if current.val == current.right.val:
            current.right = current.right.right
        else:
            current = current.right
    return head

def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.right
    return result

def remove_duplicates(arr):
    if not arr:
        return []
    linked_list = array_to_linked_list(arr)
    linked_list = delete_duplicates(linked_list)
    return linked_list_to_array(linked_list)

# 示例
input_array = [1, 1, 2, 3, 3]
output_array = remove_duplicates(input_array)
print("输出:", output_array)  # 输出: [1, 2, 3]