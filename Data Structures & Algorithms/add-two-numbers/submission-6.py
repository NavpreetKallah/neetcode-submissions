# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        summed = dummy = ListNode()

        while l1 or l2 or carry:
            l1val = l2val = 0
            if l1:
                l1val = l1.val
                l1 = l1.next

            if l2:
                l2val = l2.val
                l2 = l2.next

            total = l1val + l2val + carry
            carry = 0
            carry = total // 10
            total %= 10

            summed.next = ListNode(total)
            summed = summed.next

        return dummy.next