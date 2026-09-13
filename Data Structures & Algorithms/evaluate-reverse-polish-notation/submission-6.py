class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators="+-*/"
        res = 0
        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                if c == "+":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a+b)
                if c == "-":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b-a)
                if c == "/":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b/a)
                if c == "*":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a*b)

        
        print(stack)
        return int(stack[0])
        