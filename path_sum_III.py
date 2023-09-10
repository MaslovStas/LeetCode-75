# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<Node({self.val})>'


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        self.result = 0
        self.cache = {0: 1}
        self.target = targetSum

        self.dfs(root, 0)

        return self.result

    def dfs(self, node: TreeNode, currPathSum: int):
        if node is None:
            return

        currPathSum += node.val
        oldPathSum = currPathSum - self.target
        self.result += self.cache.get(oldPathSum, 0)
        self.cache[currPathSum] = self.cache.get(currPathSum, 0) + 1

        self.dfs(node.left, currPathSum)
        self.dfs(node.right, currPathSum)

        self.cache[currPathSum] -= 1


node1 = TreeNode(0)
node2 = TreeNode(-1, left=node1)
node3 = TreeNode(1)
node4 = TreeNode(3, left=node2)
node5 = TreeNode(1, right=node3)
node6 = TreeNode(2, left=node4, right=node5)

sol = Solution()
print(sol.pathSum(node6, targetSum=2))
