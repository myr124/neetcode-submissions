'''

[-1,[0,[1,[2,-1,-4]]]] add up to 0

hashset put in values 
(-1,0,1) (0,1,-1)

sort both tuples we get the same tuple

-1 0 1
- edge case what if no solution
- what happens when we have duplicate triplets?

for
    for
        for


sorting the list
hashset for detecting duplicates
then triple nested loop to go through every triplet*

o(n^3)
o(n)

optimized solution
- sort list X
- add elements as we loop to the set X
- for loop for every num X
- then within that we do a while loop X
- res array  X
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []

        for i in range(len(nums)):
            
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l,r = i+1, len(nums)-1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                
                if total > 0:
                    r-=1
                
                if total < 0:
                    l+=1        

        return res


        
        