'''
you are given a string s

three characters : ( ) * 

A '*' could be treated as a right parenthesis 
')' character or a left parenthesis '(' character, 
or as an empty string "".


((**)

corrector: 1

**)

standard stack logic for parenthesis but then we store a map of *
that helps us get rid of errors

stack

make map of frequency of asterisks

for c in s
if open
add to stack
if close pop
if close and stack empty check map for asterisks to replace
if asterisk count 0 return false

if stack still has elements we want to compare frequency of asterisks
with chars left if lower or equal we return true else false

'''


class Solution:
    def checkValidString(self, s: str) -> bool:

        left = []
        star = []


        for i,c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            elif c ==")":
                if not left and not star:
                    return False
                elif not left:
                    star.pop()
                else:
                    left.pop()
        
        while left and star:
            if left.pop() > star.pop():
                return False

        return not left



"((((((((()))))))))))"


        