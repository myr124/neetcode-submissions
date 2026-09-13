class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        # choices
        # constraints
        # undo choice

        res = []

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for num in nums:
                if num in cur:
                    continue
                
                cur.append(num)
                backtrack(cur)
                cur.pop() # backtracking step
        
        backtrack([])

        return res

        