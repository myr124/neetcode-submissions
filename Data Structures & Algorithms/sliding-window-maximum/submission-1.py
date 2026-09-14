'''
my idea is to use a max heap to keep track of largest values

when our window moves and if our current max is slid out we need to heappop and find the new biggest value

since our window moves only one by one i believe this should work well

actually just realized one issue, when we form a new window, we are also potentially removing values that are not max in our heap, it would be pretty inefficient to remove these without heappop       
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
        