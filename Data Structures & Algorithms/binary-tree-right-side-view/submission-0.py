# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    """
    
    append the root

    if the right exists append the right
    depth = 1

    if the right doesnt exist
    append the left, if the left doesnt exist exit this branch and continue on the left branch

    
    
    """


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            curr = None
            for _ in range(levelSize):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr.val)

        return res
    