class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums) # binary search only works on sorted or rotated
        # sorted arrays

        l = 0 # first initialize two pointers to be 0 and len or array
        r = len(nums) - 1

        while l <= r: # important to have <= because we also want to account for overlapping pointer

            m = l + ((r-l)//2) # calculate middle

            if nums[m] > target: # check if middle matches target if less than we move left pointer to above m so that we look at bigger half
                r = m - 1
            elif nums[m] < target: # inverse logic for above
                l = m + 1
            else:
                return m
        
        return -1
        