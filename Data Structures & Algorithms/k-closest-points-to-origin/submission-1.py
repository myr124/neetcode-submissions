import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        vals = []
        for i in range(len(points)):
            x = (points[i][0]-0)**2 + (points[i][1]-0)**2
            print(x)
            vals.append((math.sqrt(x),points[i]))
            print(math.sqrt((points[i][0]-0)**2 + (points[i][1]-0)**2))
            #                       sqrt((x1 - x2)^2 + (y1 - y2)^2))

        heapq.heapify(vals)

        return [heapq.heappop(vals)[1] for _ in range(k)]
