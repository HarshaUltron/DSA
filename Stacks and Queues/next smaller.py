class Solution:
    def nextSmaller(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(n):

            # Current element is smaller than
            # elements waiting in the stack
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]

            # Store index, not value
            stack.append(i)

        return result