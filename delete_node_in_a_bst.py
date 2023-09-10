# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<Node {self.val}>'


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right is None or root.left is None:
                return root.right or root.left

            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def show_tree(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        return self.show_tree(root.left) + [root.val] + self.show_tree(root.right)


node1 = TreeNode(1)
node3 = TreeNode(3)
node7 = TreeNode(7)
node8 = TreeNode(8, left=node7)
node11 = TreeNode(11)
node10 = TreeNode(10, right=node11)
node13 = TreeNode(13)
node12 = TreeNode(12, left=node10, right=node13)
node9 = TreeNode(9, left=node8, right=node12)
node2 = TreeNode(2, left=node1, right=node3)
node4 = TreeNode(4, left=node2, right=node9)


sol = Solution()
print(Solution().show_tree(node4))
sol.deleteNode(node4, 12)
print(Solution().show_tree(node4))
