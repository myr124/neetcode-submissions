class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(root,val):
            if root == None:
                return TreeNode(val)

            if val > root.val:
                root.right = insert(root.right, val)
            elif val < root.val:
                root.left = insert(root.left,val)
            return root
        
        root = insert(root,val)

        return root