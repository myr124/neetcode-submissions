# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameTree(root, root2):
            if not root and not root2:
                return True
            elif not root or not root2:
                return False

            left = isSameTree(root.left,root2.left)
            right = isSameTree(root.right,root2.right)

            return left and right and root.val == root2.val
        

        return isSameTree(p,q)