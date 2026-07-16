# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setS = set()
        while head != None:
            if head in setS:
                return True
            setS.add(head)
            head = head.next
        return False
        