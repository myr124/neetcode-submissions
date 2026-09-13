'''

 l r
[5,6,1,2,3,4] target = 6

move left or right pointer to correct section? then perform binary search on that section


'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l<=r:
            m = (l+r) // 2

            if nums[m] == target:
                return m

            # left sorted portion
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            
            # right sorted portion

            else:
                if target > nums[r] or target < nums[m]:
                    r= m-1
                else:
                    l=m+1
        
        return -1
        