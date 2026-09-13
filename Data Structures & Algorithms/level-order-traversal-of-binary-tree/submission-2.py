# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        res = []

        q.append(root)

        while len(q) > 0:
            temp = []
            for i in range(len(q)):
                
                curr = q.popleft()
                if curr:
                    temp.append(curr.val)
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
            if len(temp) > 0:
                res.append(temp)    
        
        return res


        