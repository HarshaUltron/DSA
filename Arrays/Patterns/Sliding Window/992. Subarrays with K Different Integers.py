# 992. Subarrays with K Different Integers
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


def atMost(nums, k):
    count = {}
    left = 0
    res = 0

    for right in range(len(nums)):
        count[nums[right]] = count.get(nums[right], 0) + 1

        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        # number of subarrays ending at right
        res += (right - left + 1)

    return res


class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return atMost(nums, k) - atMost(nums, k - 1)
    


# exactly(k) = atMost(k) - atMost(k-1)
# 🔥 Why This Works
# atMost(k) → subarrays with ≤ k distinct
# atMost(k-1) → subarrays with ≤ k-1 distinct

# 👉 Subtract → you get exactly k