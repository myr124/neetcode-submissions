'''

decision tree
we either add or subtract from our list

we do a recursive function
that appends to our res with the sublist we currently have
then we recurse with a list that is popped and also added
we use a set to store sublists and when we run into duplicates
we break

res = set()

def recurse(list,index):
    if list in set:
        return
    if not list:
        return
    
    set.add(list)
    add = list + nums[index+1]
    list.pop(0)
    del = list
    recurse(add,index+1)
    recurse(del, index-1)

return res

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def recurse(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # two choices
            
            subset.append(nums[i])
            recurse(i+1)

            subset.pop()
            recurse(i+1)
        
        recurse(0)
        return res
                