# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# a node is considered good if the path from root to that node contains no value

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = []

        def dfs(root,maxVal):

            if not root:
                return None
            
            if root.val >= maxVal:
                res.append(root.val)

            dfs(root.left, max(maxVal,root.val))
            dfs(root.right, max(maxVal,root.val))


        dfs(root,float("-inf"))
        return len(res)    

        