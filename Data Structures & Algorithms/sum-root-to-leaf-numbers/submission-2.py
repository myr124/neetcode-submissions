# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0 
        path = []
        numbers = []
        def dfs(root, path):
            if not root:
                return
            
            
            path.append(str(root.val))

            dfs(root.left,path)
            dfs(root.right,path)

            if not root.left and not root.right:
                numbers.append("".join(path.copy()))
                path.pop()
            else:
                path.pop()
            
            print(path)
            
            
            
        
        dfs(root,path)

        for i in numbers:
            res+=int(i)

        return res