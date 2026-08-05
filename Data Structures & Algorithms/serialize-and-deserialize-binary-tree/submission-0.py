# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    """



    """
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            if not root:
                return "N|"
            string = f"{root.val}|"
            return string + helper(root.left) + helper(root.right)
        return helper(root)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        listData = [int(n) if n != "N" else None for n in data.split("|")[:-1]]
        if not listData[0]:
            return None

        def dfs(root, listData):
            if not root or not listData:
                return None
            left = listData.pop(0)
            if left:
                root.left = TreeNode(left)
                dfs(root.left, listData)
            right = listData.pop(0)
            if right:
                root.right = TreeNode(right)
                dfs(root.right, listData)

        root = TreeNode(listData.pop(0))
        dfs(root, listData)

        return root

        
