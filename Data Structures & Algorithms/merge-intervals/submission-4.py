'''
given an array of intervals where
merge all overlapping intervals
and return array of non overlapping intervals that cover
all intervals in the input

Input: intervals = [[1,3],[1,5],[6,7]]
[1,3],[1,5] overlap so we merge
to [1,5] (min of starts and max of ends)
how is overlap detected 
3 was in between 1,5
1 matches 1
Output: [[1,5],[5,7]]

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]

clarifying question are intervals sorted?

these scenarios show overlapping intervals in one instance
but what if intervals overlap multiple times?

we dont make changes to array just yet, we keep an overlapped interval
until there are no overlaps with that interval with the next one

flow

take one interval compare with next if overlap merge and store
merge in a variable if no overlap append both store next as in
that merge variable and continue

edge case
what if like in example 2 we just merge and never run into 
a non-overlapping interval

after loop just check

pseudo code

sorted_arr = sorted(intervals)

merged = first element

res = []

for i in intervals(till end excluding first):
    check for overlap between i and merged:
        if overlap:
            merge and store in merged
        elif not:
            store i in merged
            append merged to res
    

res.append(merged)

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalSorted = sorted(intervals)
        res = []
        merged = intervalSorted[0]

        for i in range(1,len(intervalSorted)):
            if (intervalSorted[i][0] >= merged[0] and intervalSorted[i][0] <= merged[1]) or (intervalSorted[i][1] >= merged[0] and intervalSorted[i][1] <= merged[1]):
                merged = [min(merged[0],intervalSorted[i][0]),max(merged[1],intervalSorted[i][1])]
            else:
                res.append(merged)
                merged = intervalSorted[i]
                
        
        res.append(merged)

        return res

        