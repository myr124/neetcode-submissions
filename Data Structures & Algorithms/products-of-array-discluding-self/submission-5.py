'''
UPI
Understand
We are given an array nums where we need to return an array where each corresponding index is the product of every number in the input array except for the number in that specific index
recommended runtime is o(n) and space is also o(n)
Plan
We could brute force or use division ofc

essentially for division we get the total product and then just divide that
by the number in the current index
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeroCount = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                zeroCount += 1
        
        if zeroCount > 1:
            return [0]*len(nums)

        print(product)
        for a in nums:
            if a!=0:
                if zeroCount>0:
                    res.append(0)
                else:
                    res.append(int(product/a))
            else:
                res.append(product)
        return res 
        