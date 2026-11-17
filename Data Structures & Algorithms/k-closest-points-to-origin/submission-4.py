'''
given a 2d array points where points[i] = [xi,yi] we are also given an integer k

we have to return the k closest points to the origin (0,0)

you may return the answer in any order, answer is guranteed to be unique 

we can have negative values as points X

what if we have two distances that are tied can we return either? X

brute force:

calculate all distances between a point and origin, sort these distances and return k values from this slice. we should map the distance to the actual point so we know which distance is for which point, if we have tied distances we need to make sure that we are only return k number of points

distances cant be tied and that every point has its own unique distance from origin to the point

1. calculate distances, we append a tuple (distance, point)
2. sort by distance
3. we iterate k times and add those points to array and return array



'''


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        res = []

        for point in points:
            distances.append((math.sqrt(((point[0]-0)**2) + (point[1]-0)**2),point))
        

        heapq.heapify(distances)

        for i in range(k):
            val = heapq.heappop(distances)
            res.append(val[1])
        

        return res
        