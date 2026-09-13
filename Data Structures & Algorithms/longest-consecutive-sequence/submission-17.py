'''
integer nums

return length of lcs of elements that can be formed

lcs - element is exactly 1 greater than previous

[0,3,2,5,4,6,1,1]
[2, 3, 4, 4, 5, 10, 20]

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        count = 0

        for i in numSet:
            length = 0

            if i-1 not in numSet:
                while i+length in numSet:
                    length += 1
            
            count = max(count, length)


        return count
            