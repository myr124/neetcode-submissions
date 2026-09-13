'''
array of length n - sorted in ascending order, but has been rotated between 1 and n times

nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.


    min = float(inf)
       l       r      
    [6,1,2,3,4,5] o(n)
             l   
             r
    [3,4,5,6,1,2]

    l = 0
    r= 5
    0+5 // 2  = 
-unique elements
-return minimum element array

suboptimal:
running min that updates when we run into smaller value o(n) runtime
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l],res)
                break
            
            m = (l+r) // 2
            
            res = min(nums[m],res)

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        
        return res

