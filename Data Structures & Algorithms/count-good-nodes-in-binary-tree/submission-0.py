# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        val = float("-inf")
        def dfs(val, root: TreeNode):
            if not root:
                return 0
            
            if root.val >= val:
                print(root.val)
                print(val)
                res.append(root.val)
                print(res)
    
            dfs(max(root.val,val), root.left)
            dfs(max(root.val,val), root.right)


        
        dfs(val, root)
        print(res)
        return len(res)
        
