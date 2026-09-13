'''
you are given a 2d array intervals

array queries, try to find a interval where value in those indices exist
and on top of that it has to be the shortest one

we have to find interval where value resides
what are the solutions to that
binary search using intervals?
or linear search after sorting

nlogn for sort
n for traversal

sort array
linear search to find interval, check if there are smaller ones and
update min length as traversing then input that length in res array

this is brute force

'''


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = []

        for i in queries:
            m = float('inf')
            for j in intervals:
                if i >= j[0] and i<= j[1]:
                    print("yes")
                    m = min((j[1]-j[0]+1),m)
            if m == float('inf'):
                m = -1
            res.append(m)

        return res
        