class Solution:
    def preToPost(self, s):
        stack = []

        for x in reversed(s):
            if x.isalnum():
                stack.append(x)
            else:
                left = stack.pop()
                right = stack.pop()

                stack.append(left + right + x)
                print(stack)
        
        return stack[-1]

df=Solution()
print(df.preToPost("+a*bc"))    