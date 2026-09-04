class Solution:
    def isValid(self, s: str) -> bool:

        dictt={
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                if(stack[-1]==dictt[i]):
                    stack.pop()
                else:
                    return False

       # stack should be empty
        return len(stack) == 0
        