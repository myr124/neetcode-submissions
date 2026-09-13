# eliminate duplicates using a set
# utilize o(1) lookup to see if n+1 exists if it does add one to streak
# do this for all values until done
# keep a max counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0
        streak = 1
        for i in nums:
            if i-1 not in numSet:
                while i+streak in numSet:
                    streak+=1
                count = max(streak,count)
                streak = 1
        
        return count


    

        