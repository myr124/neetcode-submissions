# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
input: non-empty binary tree
output: max path sum of any non-empty path (int)


running max res non local variable


A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

check max of each subtree and compare it with res (this is our decision to split), we also take largest running path we have and also compare with res, this is also what we return (decision to not split and extend path by one more level) 

'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float('-inf')

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(max(max(root.val+left,root.val+right),root.val),root.val+right+left,res)

            return max(max(root.val+left,root.val+right),root.val)
        
        dfs(root)

        return res


        