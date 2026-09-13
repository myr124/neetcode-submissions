"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        
        oldtoNew = {}

        def dfs(root):
            if root in oldtoNew:
                return oldtoNew[root]
            
            copy = Node(root.val)
            oldtoNew[root] = copy

            for neighbor in root.neighbors:
                copy.neighbors.append(dfs(neighbor))
        
            return copy
        
        
        
        return dfs(node) if node else None
        
        