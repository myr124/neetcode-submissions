'''
array of ints nums, find subarray with largest sum and return sum
input: array of ints
output: largest sum from a subarray

values can be negative obviously cause if array is completely positive
you just return entire array

we grow a window until window is no longer positively adding to our sum

then we reset window so that we start off fresh that is actively adding to our array


currsum = 0
maxsum = float("-inf")
for r in range(len(nums)):
    if currsum is less than 0 aka negative:
        currsum = 0
    currsum += nums[r]
    maxsum = max(currsum, maxsum)

return maxsum


'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currsum = 0
        maxsum = nums[0]
        for r in range(len(nums)):
            if currsum < 0:
                currsum = 0
            currsum += nums[r]
            maxsum = max(currsum, maxsum)

        return maxsum

    
        