# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<Node {self.val}>'


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        q = deque([(root, 1)])
        res, curr_deep = [], 0
        while q:
            node, deep = q.popleft()
            if deep != curr_deep:
                res.append(node.val)
                curr_deep = deep
            if node.right:
                q.append((node.right, deep + 1))
            if node.left:
                q.append((node.left, deep + 1))
        return res


node4 = TreeNode(4)
node2 = TreeNode(2, left=node4)
node3 = TreeNode(3)
node1 = TreeNode(1, left=node2, right=node3)
print(Solution().rightSideView(node1))
