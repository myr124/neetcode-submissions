# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
main difficulty is to account for two cases

case 1: node being deleted has zero or one children
case 2: node being deleted has two children

"""


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMin(root):
            while root and root.left:
                root = root.left
            return root
        
        def delete(root, val):
            if root == None:
                return None
            
            if val < root.val:
                root.left = delete(root.left, val)
            elif val > root.val:
                root.right = delete(root.right, val)
            else:
                # case 1
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = findMin(root.right)
                    root.val = minNode.val
                    root.right = delete(root.right, root.val)
            
            return root

        
        root = delete(root,key)

        return root