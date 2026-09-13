class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        curcomb = []
        def combine(i,curcomb,k):
            if len(curcomb) ==k:
                res.append(curcomb.copy())
                return
            if i > n:
                return
            
            for j in range(i,n + 1):
                curcomb.append(j)
                combine(j+1,curcomb,k)
                curcomb.pop()
        
        combine(1,curcomb,k)
        
        return res
