import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1

            if x < y:
                heapq.heappush(stones,(y-x)* -1) 
            else:
                heapq.heappush(stones, (x-y)* -1) 
            print(stones)
        
        if stones:
            print(stones)
            return stones[0] * -1
        return 0