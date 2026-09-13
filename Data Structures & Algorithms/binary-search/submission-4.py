'''
- array of distinct integers nums
- sorted
- integer target
- implement function to search for target within nums, if it doesnt exist return -1
Your solution must run in O(logn) time.

brute force:
linear scan - o(n) X does not satisfy

optimized:
binary search (its in the name :) )
- two pointers
- eliminate half choices every iteration through a middle calculation
                
             l     r
nums = [-1,0,2,4,6,8], target = 4
        0      m    5

while l < r

0+5 = 5//2 = 2
nums[m] < target so we move l to m+1 (? maybe just m but we alr evaluated m)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [-1,0,2,4,6,8]
        0           5         
        
        0 + ( (5-0)//2 )
        '''
        l, r  = 0, len(nums)-1

        while l <= r:
            # (l+r) // 2
            m = (l+r) // 2

            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        
        return -1

        