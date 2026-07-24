# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        count = 0
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
            count += 1

        stack = stack[count//2:]

        curr = head

        while stack:
            tail = stack.pop()
            if curr:
                temp = curr.next
                curr.next = tail
                tail.next = temp
                curr = temp
            else:
                break

        if curr:
            curr.next = tail
        tail.next = None


        