# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
        Plan:
        Calculate current height by adding 1 to height of node below
        Diameter = height of left + right subtree
        
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
    
    def maxHeight(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
