# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
find is binary tree is balanced
so we are given a binary tree, we have to compare left and right subtrees to see if difference in height is no more than 1
thats the balanced

so my strategy


-dfs
=postorder reach leaf process send back to calculate difference in height and see if its higher than one


def dfs(root, height):
    if not root:
        return True
    
    leftDiff = dfs(root.left, height + 1)
    rightDiff = dfs(root.right, height + 1)

    if leftDiff - rightDiff > 1:
        return False
    else:
        return True
'''


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
               return [True, 0]
            
            leftDiff = dfs(root.left)
            rightDiff = dfs(root.right)

            balanced = (leftDiff[0] and rightDiff[0] and abs(leftDiff[1] - rightDiff[1]) <= 1)

            return [balanced,max(leftDiff[1],rightDiff[1])+1]
        

        return dfs(root)[0]