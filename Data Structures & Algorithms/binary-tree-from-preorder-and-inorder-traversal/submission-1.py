# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
loop through inorder and create neighbors map
2: [null, 1]
1: [2,3]
3: [1,4]

notice there are duplicates, we can replace those with nulls

now we loop through preorder

first we hit one, we make that the root and assign it 2 and 3
add one to some visit set
then we go to 2 (maybe we can do dfs until we hit two)
we repeat what we did with 1 but we check if any neighbor has already
been visited if they have we make that child a null instead of the number
whenever we add a number we add it to visit

what if duplicates?
if we run into duplicates we can tweak our approach to have our neighbors
also hold indices in form (node.val, index from inorder arr), then
when we do comparison we know its the same node 

we know root is always going to be preorder[0]
then we can create relations
kinda inefficient 

pseudo
map = {}
for loop thru inorder
    check i-1 and i+1 if within bounds and add as neighbors

root = newNode(preorder[0])

def dfs(root):
    if not root:
        return
    
    left = map[root.val][0]
    right = map[root.val][1]
    
    if left in visit:
        root.left = null
    else:
        root.left = newNode(left)
    if right in visit:
        root.right = null
    else:
        root.right = newNode(right)
    
    dfs(root.left)
    dfs(root.right)

return root
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
            

        