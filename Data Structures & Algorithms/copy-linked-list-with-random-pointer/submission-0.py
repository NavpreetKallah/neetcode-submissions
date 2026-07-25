"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    
    problem: we do not know where the randoms point

    by storing the index where the nodes occur when a random points to them we know the link
    in random links we have the point positions of each node e.g 1 points to 4


    

    
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pos = {}
        randomLinks = {}
        randomsCopy = {}
        count = 0
        curr = head
        copy = Node(0)

        while curr:
            pos[curr] = count
            count += 1
            curr = curr.next

        curr = head
        copyCurr = copy
        count = 0
        while curr:
            copyCurr.next = Node(curr.val)
            copyCurr = copyCurr.next

            randomLinks[count] = pos.get(curr.random,-1)
            randomsCopy[count] = copyCurr

            count += 1
            curr = curr.next

        print(randomLinks)

        count = 0
        curr = copy.next
        while curr:
            curr.random = randomsCopy.get(randomLinks[count], None)
            count += 1
            curr = curr.next

        return copy.next

        
