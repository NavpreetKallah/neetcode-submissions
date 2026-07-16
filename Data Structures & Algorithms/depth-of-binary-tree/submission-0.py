# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = -1
        return self.findMax(root, curr)

    def findMax(self, node: TreeNode, curr):
        if node != None:
            curr = max(self.maxDepth(node.left),self.maxDepth(node.right))
        return curr + 1