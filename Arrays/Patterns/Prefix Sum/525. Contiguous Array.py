# 525. Contiguous Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        prefix_sum = 0
        n_dict = {}
        m_len = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum == 0:
                m_len = i + 1

            elif prefix_sum in n_dict:
                m_len = max(m_len, i - n_dict[prefix_sum])

            if prefix_sum not in n_dict:
                n_dict[prefix_sum] = i

        return m_len