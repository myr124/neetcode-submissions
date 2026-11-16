'''
you are given an array of intgers stones where stones[i] represents the weight of the ith stone.

we can get two heaviest with heap and heappop

do conditions and whatever they ask for

ig a destroyed stone can be a zero - yeah this works

count how many non-zero stones exist

1. heapify (max heap so negative numbers)
2. while true loop breaks when two largest are a number and zero (indicating one remaining stone)
3. loop through to count number of stones

2 and 3 could be better


'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        
        heap = stones
        res = 0

        for i in range(len(heap)):
            heap[i] = heap[i] * -1

        heapq.heapify(heap)
        
        '''
        [6,4,3,2,2]
        6
        4

        1,2
        '''


        while len(heap) > 1:
            y = heapq.heappop(heap) * -1
            x = heapq.heappop(heap) * -1

            print(x)
            print(y)
            

            if x < y:
                y = y - x
                x = 0
                maxval = max(x,y)
                print(maxval)
                heapq.heappush(heap,maxval*-1)
            
            


        for stone in heap:
            if stone*-1 > 0:
                res = stone*-1

        return res
            
        