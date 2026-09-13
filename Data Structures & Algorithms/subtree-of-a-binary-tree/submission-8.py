# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
root and subroot
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root,subroot):
            if not root and not subroot:
                return True
            
            elif not root or not subroot:
                return False

            left = sameTree(root.left, subroot.left)
            right = sameTree(root.right, subroot.right)

            return left and right and root.val == subroot.val

        def dfs(root, subroot):
            if not root:
                return False

            if sameTree(root,subroot):
                return True
            
            left = dfs(root.left, subroot)
            right = dfs(root.right, subroot)

            return left or right

            
        return dfs(root,subRoot)
        