import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        for i,k in enumerate(self.nums):
            self.nums[i] *= -1

        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val*-1)
        val = heapq.nsmallest(self.k, self.nums)
        print(val)
        return val[-1] * -1
