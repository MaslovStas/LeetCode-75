# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left)) if root else 0


node_9 = TreeNode(9)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, left=node_15, right=node_7)
node_3 = TreeNode(3, left=node_9, right=node_20)

sol = Solution()
print(sol.maxDepth(node_3))
