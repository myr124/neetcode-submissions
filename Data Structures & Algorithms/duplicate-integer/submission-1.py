class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDup = set()
        for e in nums:
            if e in checkDup:
                return True
            checkDup.add(e)
        return False

        
         