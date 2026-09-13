'''
2d array of integers triplets where triplets[i] = [ai, bi, ci] represents
the ith triplet
you also given an array of integers target = [x,y,z]

operation = take two triplets and return new triplet that is the max values of
both

you can do this zero or more times

brute force

take each array and check if its target
if its target lets iterate through rest of values
and max to see if it fits target

we only need to run max operation through triplets[i] and onwards no before
entries

'''

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()

        for n in triplets:
            if n[0] > target[0] or n[1] > target[1] or n[2] > target[2]:
                continue
            
            for i,v in enumerate(n):
                if v == target[i]:
                    good.add(i)
            
        
        return True if len(good) == 3 else False

                    

        