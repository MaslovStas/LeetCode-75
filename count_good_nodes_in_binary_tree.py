class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<Node(val={self.val})>'


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val=float('-inf')):
            if node is None:
                return 0
            max_val = max(max_val, node.val)
            return (node.val == max_val) + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root)


node_6 = TreeNode(6)
node_3 = TreeNode(3, left=node_6)
node_9 = TreeNode(9, right=node_3)

sol = Solution()
print(sol.goodNodes(node_9))
