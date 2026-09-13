'''

give array han
where hand[i] is
value written on ith card and int groupsize

you want to rearrange the cards into groups
so that each group is of size groupSize and card values
are consecutively increasing by 1

return true if possible, false if not

cards have to be consecutive and also in the groupsize length subarrays

arrays are not sorted

if we sort we get values in a consecutive order, then we try to generate
arrays based on group size

we could use a min heap and store values in that, pop values that are consecutive

'''

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = defaultdict(int)
        for i in hand:
            m[i]+=1
        
        minH = list(m.keys())
        heapq.heapify(minH)
        
        if len(hand) % groupSize != 0:
            return False

        while minH:
            minVal = minH[0]

            for i in range(minVal, minVal+groupSize):
                if i not in m:
                    return False
                m[i] -= 1
                if m[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True


        