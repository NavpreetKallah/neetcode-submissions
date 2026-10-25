# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead = ListNode()
        rightHead = ListNode()
        curr = head
        left = leftHead
        right = rightHead
        while curr:
            if curr.val < x:
                left.next = ListNode(curr.val)
                left = left.next
            else:
                right.next = ListNode(curr.val)
                right = right.next
            curr = curr.next
        left.next = rightHead.next
        return leftHead.next
        