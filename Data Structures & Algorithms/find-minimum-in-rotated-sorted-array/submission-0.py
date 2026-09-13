class Solution:
    def findMin(self, nums: List[int]) -> int:
        def rotate(nums):
            first = nums[0]
            last = nums[len(nums)-1]
            nums[0] = last
            print(nums)
            for i in range(1,len(nums)):
                print(nums[i])
                prev = nums[i]
                nums[i] = first
                first = prev

        minIndex = nums.index(min(nums))
        numRotate = (len(nums) - (minIndex+1)) + 1

        for i in range(numRotate):
            rotate(nums)
        
        return nums[0]
                

        