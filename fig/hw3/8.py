class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # 检查当前节点是否违反二叉搜索树特性
            if self.prev.val >= node.val:
                if not self.first:
                    self.first = self.prev

                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val


def print_inorder(root):
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result


# [1,3,null,null,2] -> [3,1,null,null,2]
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)

print("输入：", print_inorder(root1))
BST().recoverTree(root1)
print("输出：", print_inorder(root1))