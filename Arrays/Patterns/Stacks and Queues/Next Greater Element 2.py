class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)

        # Answer for every element
        result = [-1] * n

        # Monotonic decreasing stack
        # Stores indices whose next greater element
        # has not been found yet.
        stack = []

        # Traverse the array twice
        for i in range(2 * n):

            # Convert circular index back into [0, n-1]
            current_index = i % n
            current = nums[current_index]

            # Current element can be the next greater
            # element for elements waiting in the stack.
            while stack and current > nums[stack[-1]]:
                index = stack.pop()
                result[index] = current

            # During the first pass, put indices into stack.
            # During the second pass, we only use elements
            # to find their greater elements.
            if i < n:
                stack.append(current_index)

        return result
df=Solution()
nums = [1, 2, 1]    
print(df.nextGreaterElements(nums))