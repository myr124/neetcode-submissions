class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = Counter(nums)

        for i in freqMap:
            if freqMap[i] > len(nums)/2:
                return i
        