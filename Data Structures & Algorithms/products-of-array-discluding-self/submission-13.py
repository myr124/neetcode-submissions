class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # product = 2
        #        x        
        # [1,2,4,6]
        # prefix = [1,1,2,8]
        # # insert into 0th index so everything gets pushed and stays in right order 
        # suffix = [48,24,6,1]

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)
        product = 1

        for i in range(1,len(nums)):
            prefix[i] = product * nums[i-1]
            product = prefix[i]
        

        product = 1
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = product * nums[i+1]
            product = suffix[i]

        

        for i in range(len(prefix)):
            output[i] = prefix[i] * suffix[i]
        
        return output


