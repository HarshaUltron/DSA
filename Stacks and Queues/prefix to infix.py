class Solution:
    
        def preToInfix(self, s):
            stack = []

            for x in reversed(s):
                if x.isalnum():
                    stack.append(x)
                else:
                    left = stack.pop()
                    right = stack.pop()

                    stack.append("(" + left + x + right + ")")

            return stack[-1]