import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)

        while k !=0:
            k-=1
            res= heapq.heappop(nums)
        
        return res * -1
            

        

        
        