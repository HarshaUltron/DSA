# 930. Binary Subarrays With Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq={}
        freq[0]=1
        count=0
        prefix=0
        for num in nums:
            prefix+=num
            count+=freq.get((prefix-goal),0)
            freq[prefix]=freq.get(prefix,0)+1
        return count    


df=Solution()
print(df.numSubarraysWithSum([1,1,1], goal = 2))         