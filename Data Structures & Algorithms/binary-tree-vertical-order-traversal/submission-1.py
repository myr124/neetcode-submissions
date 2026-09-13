# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
column traversal means going vertically
'''

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        m = defaultdict(lambda:[])
        q = deque()
        q.append((root,0))
        minCol, maxCol = 0,0

        while q:
            curr = q.popleft()
            m[curr[1]].append(curr[0].val)
            minCol = min(curr[1], minCol)
            maxCol = max(curr[1], maxCol)

            if curr[0].left:
                q.append((curr[0].left,curr[1]-1))
            if curr[0].right:
                q.append((curr[0].right,curr[1]+1))
        
        for i in range(minCol,maxCol+1):
            res.append(m[i])
        

        return res

            
        

        
        