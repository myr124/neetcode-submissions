'''
design a class
find the kth largest integer in a stream of values 
includes duplicates



[5,6]

3-2 = 1

len(values) - k

then we make that number of pops in a minheap variant



'''


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        moves = len(self.heap) - self.k

        for i in range(moves):
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
