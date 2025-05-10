class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum(root):
    def dfs(node, current_num):
        if not node:
            return 0

        current_num = current_num * 10 + node.val

        if not node.left and not node.right:
            return current_num

        return dfs(node.left, current_num) + dfs(node.right, current_num)

    return dfs(root, 0)


# 测试[1,2,3]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(f"示例1结果: {sum(root1)}")

# 测试[4,9,0,5,1]
root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)
print(f"示例2结果: {sum(root2)}")