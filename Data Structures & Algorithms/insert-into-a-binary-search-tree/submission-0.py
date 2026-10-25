# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def insert(prev, root, val):
            if not root:
                if prev.val > val:
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
                return

            if root.val > val:
                insert(root, root.left, val)
            else:
                insert(root, root.right, val)
        
        insert(None, root, val)
        return root