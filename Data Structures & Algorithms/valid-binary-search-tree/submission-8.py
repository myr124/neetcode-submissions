# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
given root of a binary tree

return true/false if it is a valid BST

the left subtree contains only nodes with keys less than node's keys

the right subtree only has values bigger than node's keys

'''


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,p,q):
            if not root:
                return True

            if not p < root.val < q:
                print(p)
                print(root.val)
                print(q)
                return False

            left = dfs(root.left,p,root.val)
            right = dfs(root.right,root.val,q)

            return left and right

        
        return dfs(root,float('-inf'),float('inf'))
        