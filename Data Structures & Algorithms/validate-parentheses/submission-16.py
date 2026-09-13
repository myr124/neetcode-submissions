'''
you are given a string s consisting of the following characters "( ) { } [ ]"

string is only valid if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

return true if s is a valid string false otherwise



""

opening = []

stacks, queues


""

runtime complexity
o(n)

space complexity
o(n)

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
