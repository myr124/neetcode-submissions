class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)

        return len(nums) != len(dup)
        