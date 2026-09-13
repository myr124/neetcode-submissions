# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        q = deque()

        q.append(root)

        while q:
            for i in range(len(q)):
                curr = q.pop()
                print(curr.val)
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)


        return root