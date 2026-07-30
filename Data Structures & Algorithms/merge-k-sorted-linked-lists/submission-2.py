# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        ls = [(l.val, i, l) for i, l in enumerate(lists) if l is not None]
        heapq.heapify(ls)

        while ls:
            val, i, l = heapq.heappop(ls)
            curr.next = l
            curr = curr.next
            if l.next:
                heapq.heappush(ls, (l.next.val, i, l.next))
        return dummy.next