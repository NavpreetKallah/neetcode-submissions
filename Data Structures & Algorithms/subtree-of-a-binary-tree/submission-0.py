# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if root:
            return self.subTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
    
    def subTree(self, root, subRoot):
        if subRoot == None and root == None:
            return True
        if subRoot and root and subRoot.val == root.val:
            return self.subTree(root.left, subRoot.left) and self.subTree(root.right, subRoot.right)
        return False

        
        