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
        dummy = ListNode(0)
        summed = dummy

        while l1curr and l2curr:
            total = l1curr.val + l2curr.val + carry
            carry = 0
            carry = total // 10
            total %= 10

            newNode = ListNode(total)

            l1curr = l1curr.next
            l2curr = l2curr.next
            summed.next = newNode
            summed = summed.next

        while l1curr:
            total = l1curr.val + carry
            carry = 0
            carry = total // 10
            total %= 10

            newNode = ListNode(total)

            l1curr = l1curr.next
            summed.next = newNode
            summed = summed.next

        while l2curr:
            total = l2curr.val + carry
            carry = 0
            carry = total // 10
            total %= 10

            newNode = ListNode(total)

            l2curr = l2curr.next
            summed.next = newNode
            summed = summed.next
        if carry:
            summed.next = ListNode(carry)

        return dummy.next