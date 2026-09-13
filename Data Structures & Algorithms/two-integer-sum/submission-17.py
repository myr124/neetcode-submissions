'''
add up to target
nums

11 - 3 = 8
 i
[3,4,5,6]

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i,c in enumerate(nums):
            diff = target - c
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    print(nums[j])
                    return [i,j]
                


        