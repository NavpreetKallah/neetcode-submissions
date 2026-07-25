# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = l1
        l2curr = l2
        carry = 0
        summed = dummy = ListNode(0)

        while l1curr or l2curr or carry:
            l1val = 0
            if l1curr:
                l1val = l1curr.val
                l1curr = l1curr.next

            l2val = 0
            if l2curr:
                l2val = l2curr.val
                l2curr = l2curr.next

            total = l1val + l2val + carry
            carry = 0
            carry = total // 10
            total %= 10

            newNode = ListNode(total)

            summed.next = newNode
            summed = summed.next

        return dummy.next