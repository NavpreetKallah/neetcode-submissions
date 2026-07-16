# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = []
        curr = head
        while(curr != None):
            reverse.insert(0, curr.val)
            curr = curr.next
        if len(reverse) > 0:
            head = ListNode(reverse[0])
            curr = head
            for el in reverse[1:]:
                node = ListNode(el)
                curr.next = node
                curr = curr.next
        return head
        