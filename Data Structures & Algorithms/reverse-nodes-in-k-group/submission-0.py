# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        groupPrev = dummy
        curr = head
        while curr:
            oldestCurr = curr
            nodes = []
            for _ in range(k):
                if curr:
                    nodes.append(curr)
                    curr = curr.next
                else:
                    return dummy.next

            for i in range(len(nodes) - 1, 0, -1):
                nodes[i].next = nodes[i-1]

            groupPrev.next = nodes[-1]
            nodes[0].next = curr
            groupPrev = nodes[0]

        return dummy.next