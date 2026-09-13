# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]):
        while root and root.left:
            root = root.left
        return root

    def findMax(self, root: Optional[TreeNode]):
        while root and root.right:
            root = root.right
        return root
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            if root.right and root.left:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
        