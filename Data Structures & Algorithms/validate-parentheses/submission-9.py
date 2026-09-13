class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "({["
        closing = ")}]"

        for c in s:
            if c in opening:
                stack.append(c)
            elif len(stack)>0:
                if c == "}":
                    ch = stack.pop()
                    if ch != "{":
                        return False
                if c == "]":
                    ch = stack.pop()
                    if ch != "[":
                        return False
                if c == ")":
                    ch = stack.pop()
                    if ch != "(":
                        return False
            else:
                return False
                
            
        return len(stack)==0