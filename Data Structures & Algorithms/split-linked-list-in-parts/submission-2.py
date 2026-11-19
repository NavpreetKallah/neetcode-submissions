# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        res = [None] * k
        counts = [0] * k
        while curr:
            n += 1
            curr = curr.next

        remainder = n % k
        length = n // k
        for i in range(k):
            if remainder > 0:
                counts[i] = length + 1
                remainder -= 1
            else:
                counts[i] = length

        curr = head
        prev = None
        for idx, count in enumerate(counts):
            if curr:
                res[idx] = curr
            for i in range(count):
                prev = curr
                curr = curr.next
            if prev:
                prev.next = None

        return res
