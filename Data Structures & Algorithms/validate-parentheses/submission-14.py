'''
you are given a string s consisting of the following characters "( ) { } [ ]"

string is only valid if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

return true if s is a valid string false otherwise



"[[][]]"

opening = []

stacks, queues


""

'''

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        openChars = "({["
        closeChars = "]})"

        if len(s) % 2 != 0:
            return False
        
        if s and s[0] in closeChars:
            return False

        for c in s:
            if c in openChars:
                stack.append(c)
            elif c in closeChars:
                if c == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                        continue
                    else:
                        return False
                if c == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                        continue
                    else:
                        return False
                if c == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                        continue
                    else:
                        return False
        


        return len(stack) == 0
