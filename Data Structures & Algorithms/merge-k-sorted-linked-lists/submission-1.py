# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()

        while True:
            minimums = [(l.val, idx) for idx, l in enumerate(lists) if l != None]
            if minimums:
                minimum = min(minimums)
                curr.next = ListNode(minimum[0])
                curr = curr.next
                lists[minimum[1]] = lists[minimum[1]].next
            else:
                break

        return dummy.next