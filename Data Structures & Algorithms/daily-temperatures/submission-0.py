'''

Return an array result where result[i] is the number of days 
after the ith day before a warmer temperature appears on a future day.

the last temp is always gonna be 0 because there is no temp higher than last index


we add values into a stack values from temp


(28,6)
(40,5)


[1,4,1,2,1,0,0]

stack = []

res= [0]*len(temperatures)

for loop thru list:
    while stack and peek(stack) < val:
        c = stack.pop()
        res[c[1]] = i-c[1]
    
    stack.append(val)


return res 


'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        peek = len(stack)-1
        res = [0]*len(temperatures)

        for i,k in enumerate(temperatures):
            while stack and stack[peek][0] < k:
                c = stack.pop()
                res[c[1]] = i-c[1]
            
            stack.append((k,i))
        
        return res
        