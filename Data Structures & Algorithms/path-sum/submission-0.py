# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def backtrack(root,val):
            if not root:
                return False
            
            if (root.val + val == targetSum) and not root.right and not root.left:
                return True
            
            if backtrack(root.left, root.val+val):
                return True

            if backtrack(root.right, root.val+val):
                return True

            return False
        return backtrack(root,0)

        