"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        pointDict = {None:None}
        while curr:
            copy = Node(curr.val)
            pointDict[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = pointDict[curr]
            copy.next = pointDict[curr.next]
            copy.random = pointDict[curr.random]
            curr = curr.next

        return pointDict[head]
            