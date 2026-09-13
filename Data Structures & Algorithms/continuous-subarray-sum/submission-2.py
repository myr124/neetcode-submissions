'''
x = n * k
0 is a mulitple of k 
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder = {}
        prefix = 0

        if len(nums) < 2:
            return False
        
        for i,l in enumerate(nums):
            prefix+= l

            r = prefix%k

            print(r)
            if r == 0 and i > 0:
                return True
            
            if r in remainder and i-remainder[r]>1:
                return True 

            if r not in remainder:
                remainder[r] = i

            

        return False