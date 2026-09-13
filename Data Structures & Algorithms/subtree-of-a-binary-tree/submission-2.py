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

        def subTree(root, subroot):
            if not subroot:
                return True
            
            if not root:
                return False

            if sameTree(root, subroot):
                return True
            return (subTree(root.left, subroot) or subTree(root.right, subroot))

            
        return subTree(root,subRoot)
        