'''
integer array nums
where each element indicates max jump len at that position

nums = [1,2,0,1,0]
1: 1 jump to nums[1]
2: jump of 2 to nums[3]
3: jump of 1 to nums[4] end of array so valid

i think the greedy choice we can make here is that we iterate through the array
we a pointer that tracks the jumps, if we land on a indice with 0 thats not
the end of array we lose

edge cases
our pointer goes over bound (easy to fix we just need to add to conditional)

l = 0

for i in range(len(nums))

    l += nums[i]

    if l > len(nums):
        return true # edge case
    if nums[l] == 0 and l < (len(nums)-1):
        return false

return true
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goalpost = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalpost:
                goalpost = i


        return True if goalpost == 0 else False
        