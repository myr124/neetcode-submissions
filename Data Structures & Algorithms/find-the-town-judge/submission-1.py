'''
town there are n people 1 to n, there is a rumor
that one of these people is secretely the town judge

if town judge exists then, town judge trusts no one

everyone except tj trusts tj

these look like edges

we could have directed edges to the judge
but if the judge has any neighbors then its invalid
how do we set a judge though

[1,5] [4,3]



n-1

'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        curr = trust[0][1]

        for a,b in trust:
            if curr != b:
                return -1
            curr = b
        
        return curr
        