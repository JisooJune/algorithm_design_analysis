from graphviz import Digraph


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        return root

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, root, val):
        if not root:
            return root
        if val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            # 节点删除逻辑
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # 找到右子树的最小节点替换当前节点
                temp = self._find_min(root.right)
                root.val = temp.val
                root.right = self._delete(root.right, temp.val)
        return root

    def _find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def visualize(self, filename):
        dot = Digraph()
        if self.root:
            self._add_nodes_edges(self.root, dot)
        dot.render(f'fig/{filename}', format='png', cleanup=True)
        print(f"树结构已保存为 {filename}.png")

    def _add_nodes_edges(self, node, dot):
        dot.node(str(node.val))
        if node.left:
            dot.edge(str(node.val), str(node.left.val))
            self._add_nodes_edges(node.left, dot)
        if node.right:
            dot.edge(str(node.val), str(node.right.val))
            self._add_nodes_edges(node.right, dot)


# 构建初始二叉搜索树
bst = BST()
data = [48, 33, 49, 47, 42, 46, 32]
for num in data:
    bst.insert(num)
bst.visualize("hw3_original_tree")

# 删除节点 33
bst.delete(33)
bst.visualize("hw3_tree_after_deletion")