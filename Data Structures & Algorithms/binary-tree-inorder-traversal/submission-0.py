# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, root: Optional[TreeNode], addedList):
        if not root:
            return None
        self.recursion(root.left,addedList)
        addedList.append(root.val)
        self.recursion(root.right,addedList)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(root,res)

        return res
