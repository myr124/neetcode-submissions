class Solution:
    def isValid(self, s: str) -> bool:
        res = True
        stack = []
        opening = "({["
        closing =")}]"
        poppedval =""
        if len(s)%2!=0:
            return False
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