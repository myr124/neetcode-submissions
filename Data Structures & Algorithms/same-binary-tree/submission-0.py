# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        plist = []
        qlist = []
        def dfs(root, l):
            if not root:
                l.append(None)
                return None
            
            l.append(root.val)
            dfs(root.left, l)
            dfs(root.right, l)
        
        dfs(p, plist)
        dfs(q, qlist)

        return qlist == plist
        

        
        