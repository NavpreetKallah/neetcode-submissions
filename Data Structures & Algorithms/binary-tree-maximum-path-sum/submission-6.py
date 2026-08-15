# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")
        self.search(root)
        return self.best


    def search(self, root):
        if not root:
            return 0


        left = self.search(root.left)
        right = self.search(root.right)
        curr = root.val + left + right

        
        self.best = max(curr, self.best)

        return max(root.val + max(left, right), 0)

