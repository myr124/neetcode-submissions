class Solution:
    def isValid(self, s: str) -> bool:
        res = True
        stack = []
        opening = "({["
        closing =")}]"
        poppedval =""
     
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if stack:
                    poppedval = stack.pop()
                else:
                    return False
                if c == ")":
                    if poppedval !="(":
                        return False
                if c == "}":
                    if poppedval !="{":
                        return False
                if c == "]":
                    if poppedval !="[":
                        return False

        if stack:
            return False
        return res