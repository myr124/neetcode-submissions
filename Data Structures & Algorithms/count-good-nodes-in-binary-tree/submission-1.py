# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
how to keep track of ancestor nodes and their values and

array with max function to find biggest at the point
keep track of max value at that point
dfs approach


- dfs traversal
- preorder traversal
- keep track of max, if node val is bigger its a good node and a new max is set which is passed down recursively
- global variable list that holds these good nodes and gets appended to by the dfs
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        val = float("-inf")
        res = []


        def dfs(root, val):
            if not root:
                return None
            

            if root.val >= val:
                res.append(root.val)
                val = root.val

            dfs(root.left, val)
            dfs(root.right, val)


        dfs(root, val)

        return len(res)    
            


