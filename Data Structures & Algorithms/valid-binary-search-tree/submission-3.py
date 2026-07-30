# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
     2
    1 3

    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)
        
    def helper(self, root, minimum=-1001, maximum=1001):
        if not root:
            return True

        if not (minimum < root.val < maximum):
            return False

        return self.helper(root.left, minimum, root.val) and self.helper(root.right, root.val, maximum)