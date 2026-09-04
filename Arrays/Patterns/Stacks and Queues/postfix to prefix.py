class Solution:
    def postToPre(self, s):
        stack = []

        for x in s:
            if x.isalnum():
                stack.append(x)
            else:
                right = stack.pop()
                left = stack.pop()

                stack.append(x + left + right)

        return stack[-1]