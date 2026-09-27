# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next 
        slow.next = None

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start, middle = head, prev
        while start and middle:
            startNext = start.next
            middleNext = middle.next

            start.next = middle
            middle.next = startNext

            start = startNext
            middle = middleNext





        



        
        