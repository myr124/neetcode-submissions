class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        print(nums)

        for i in range(k):
            res = heapq.heappop(nums)
            print(res)

        return res*-1
            
        