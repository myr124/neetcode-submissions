class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testSet = set()
        for i in nums:
            testSet.add(i)
        
        if len(testSet) == len(nums):
            return False
        return True
        