# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = head
        slow, fast = head, head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        middle = prev

        while middle and start:
            if middle.val != start.val:
                return False
            middle = middle.next
            start = start.next
        return True
    