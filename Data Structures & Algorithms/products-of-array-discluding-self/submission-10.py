class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        output = [0] * n

        prefix[0] = suffix[n-1] = 1

        for i in range(1,len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(len(nums)):
            output[i] = suffix[i]*prefix[i]


        return output

