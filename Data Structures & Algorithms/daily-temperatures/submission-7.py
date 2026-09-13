'''
brute force:
- nested for loop to check when temps get higher


[0,0,0]

loop thru numbers

appending these (val,index)

[30,38,30,36,35,40,28]
[1,4,1,0,0,0,0]
[(40,5)]

- we check top of stack we check if current value that we're appending is bigger
- if it is we keep on popping until we can't no more we hit a larger number or no more values
- as we're popping we put difference of indexes
- by the end we have the completed list of results

optimize:
- with a stack
- append to a stack

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0 for i in range(len(temperatures))]


        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                temp = stack.pop()
                result[temp[0]] = i - temp[0] 

            stack.append([i, t])

        return result
        