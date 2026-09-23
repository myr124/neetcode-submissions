'''
add up to target
nums

7 - 4 = 3
 i

{3:0 ,}

[4,5,6,3]

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # o(n^2)

        map = {}

        for i,c in enumerate(nums):
            
            diff = target-c
            
            if diff in map:
                return [map[diff],i]
            else:
                map[c] = i
                


        