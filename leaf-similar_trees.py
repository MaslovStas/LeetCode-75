# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(root: TreeNode | None) -> list:
            if not root:
                return []
            if not (root.right or root.left):
                return [root.val]
            return dfs(root.right) + dfs(root.left)
        return dfs(root1) == dfs(root2)


node_1_6 = TreeNode(6)
node_1_7 = TreeNode(7)
node_1_4 = TreeNode(4)
node_1_9 = TreeNode(9)
node_1_8 = TreeNode(8)

node_1_2 = TreeNode(2, left=node_1_7, right=node_1_4)
node_1_1 = TreeNode(1, left=node_1_9, right=node_1_8)
node_1_5 = TreeNode(1, left=node_1_6, right=node_1_2)

node_1_3 = TreeNode(1, left=node_1_5, right=node_1_1)

node_2_6 = TreeNode(6)
node_2_7 = TreeNode(7)
node_2_4 = TreeNode(4)
node_2_9 = TreeNode(9)
node_2_8 = TreeNode(8)

node_2_5 = TreeNode(5, left=node_2_6, right=node_2_7)
node_2_2 = TreeNode(2, left=node_2_9, right=node_2_8)
node_2_1 = TreeNode(1, left=node_2_4, right=node_2_2)

node_2_3 = TreeNode(1, left=node_2_5, right=node_2_1)

sol = Solution()
print(sol.leafSimilar(node_1_3, node_2_3))
