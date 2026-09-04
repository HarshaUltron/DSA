# 209. Minimum Size Subarray Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        left = 0
        sliding_sum = 0

        for i in range(n):
            sliding_sum += nums[i]   # ✅ expand first

            while sliding_sum >= target:
                min_len = min(min_len, i - left + 1)  # ✅ correct length
                sliding_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
