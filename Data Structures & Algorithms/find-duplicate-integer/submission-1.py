class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dup = set()
        
        for i in nums:
            if i not in dup:
                dup.add(i)
            else:
                return i
        