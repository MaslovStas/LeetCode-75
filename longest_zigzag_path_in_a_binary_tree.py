# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        max_length: int = 0

        def dfs(node: TreeNode | None, cur_length: int = 0, direction: str = ''):
            if not node:
                return

            nonlocal max_length
            max_length = max(max_length, cur_length)

            dfs(node.left, cur_length + 1 if direction != 'left' else 1, 'left')
            dfs(node.right, cur_length + 1 if direction != 'right' else 1, 'right')

        dfs(root)
        return max_length


node1 = TreeNode(1)
node2 = TreeNode(1, right=node1)
node3 = TreeNode(1, left=node2)

node5 = TreeNode(1)
node6 = TreeNode(1, left=node5)
node7 = TreeNode(1, left=node6)

node4 = TreeNode(1, left=node3, right=node7)

sol = Solution()
print(sol.longestZigZag(node4))
