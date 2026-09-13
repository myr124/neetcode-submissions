class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curcomb = []
        
        def combine(i, curcomb, s):
            
            if s == target:
                res.append(curcomb.copy())
                return
            
            if i >= len(candidates) or s > target:
                return

            curcomb.append(candidates[i])
            combine(i+1, curcomb, s + candidates[i])
            curcomb.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            combine(i+1, curcomb, s)
        
        combine(0, curcomb, 0)

        return res