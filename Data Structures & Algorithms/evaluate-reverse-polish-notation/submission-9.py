'''
tokens represents 'valid' arithmetic sequence in RPN
return integer that represents the evaluation of the expression


The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

[1,2,+,3,*,4,-]


[5]

a = stack.pop()
b = stack.pop()

stack.append(a-b)

return stack[0]
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "*-+/"
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()

                if i=='-':
                    stack.append(int(b-a))
                if i=='/':
                    stack.append(int(b/a))
                if i=='+':
                    stack.append(int(b+a))
                if i=='*':
                    stack.append(int(b*a))
        
        '["1","2","+","3","*","4","-"]'
        '[5]'
        
        return stack[0]
                
        