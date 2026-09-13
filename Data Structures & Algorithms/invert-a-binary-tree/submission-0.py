# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root == None:
                return None
            
            oldLeft = root.left
            root.left = root.right
            root.right = oldLeft
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return root
        