# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        freq={}
        count=0
        freq[0]=1
        for num in nums:
            prefix_sum+=num
            count+=freq.get((prefix_sum-k),0)
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count    
        

df=Solution()
print(df.subarraySum([1,1,1], k = 2))
        