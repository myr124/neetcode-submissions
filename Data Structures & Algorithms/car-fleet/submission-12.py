'''
n cars traveling to same destination on a one-lane highway

You are given two arrays of integers position and speed, both of length n.

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)


you are also given a target


Input: target = 10, position = [1,4], speed = [3,2]

Output: 1

1 4 7 10
4 6 8 10

1 10-1 = 9
9//3 = 2

4
6//2 = 3

- same number of iterations taken so they become fleet

- only cars in





Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3

(4,3), (1,4), (0,10), (7,3)

(0,10) (1,4) (4,3) (7,3)

(8,2)







(7,3)



(8,4)






res = 4

* for popping we pop all the time but we only add to res when the tuple is faster


'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tupList = []
        stack = []
        res = 0


        for i in range(len(position)):
            tupList.append((position[i],(target-position[i])/speed[i]))
        
        tupList.sort(reverse=True)

        print(tupList)

        for i in tupList:
            stack.append(i)
            if len(stack) >= 2 and stack[-1][1] <= stack[-2][1]:
                stack.pop()

        
        return len(stack)
        


'''

target=100
position=[0,2,4]
speed=[4,2,1]

(0,98) (2,49) (4,96)


(1,98)
(4,96)
'''
