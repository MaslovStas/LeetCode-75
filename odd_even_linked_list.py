# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'<ListNode({self.val})>'


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        odd = head
        even = first_even = head.next

        while odd and even and odd.next and even.next:
                odd.next = even.next
                odd = even.next
                even.next = odd.next
                even = odd.next

        odd.next = first_even
        return head


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

sol = Solution()
head = sol.reverseList(node1)

cur = node1
while cur:
    print(cur.val)
    cur = cur.next
