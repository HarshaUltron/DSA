class Solution:
    def postToInfix(self, s):
        stack = []

        for x in s:
            if x.isalnum():
                stack.append(x)
            else:
                right = stack.pop()
                left = stack.pop()

                stack.append("(" + left + x + right + ")")

        return stack[-1]
df=Solution()
print(df.postToInfix(s = "ab*c+" ))    