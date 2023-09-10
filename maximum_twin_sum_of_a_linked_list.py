# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'<ListNode({self.val})>'


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, cur = None, slow
        while cur:
            prev, cur.next, cur = cur, prev, cur.next

        max_sum = 0
        while prev:
            max_sum = max(max_sum, prev.val + head.val)
            head, prev = head.next, prev.next

        return max_sum


node7 = ListNode(7)
node6 = ListNode(6, node7)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

sol = Solution()
print(sol.pairSum(node1))
